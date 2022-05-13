from flask import Flask
import base64
import json

from packages import Order, requests


username = ""
password = ""
use_sandbox = False

s3_username = ""
s3_password = ""
s3_storage_bucket = ""



app = Flask(__name__)


@app.route('/orders/<order_id>/shipping', methods=['POST'])
def add_shipping(order_id: str):
    try:
        order = Order.objects.filter(order_id=order_id).first()

        request_json = json.dumps(
            {
                "recipent": {
                    "name": order.customer.name,
                    "address": order.customer.address,
                    "city": order.customer.city,
                },
                "sender": {
                    "name": "ACME oy",
                    "address": "Fishers road 1",
                    "city": "Helsinki",
                },
                "direction": "OUTBOUND",
                "reference": order_id,
            }
        )

        dhl_response = requests.post(
            f"https://wsbexpress.dhl.com/rest/gbl/shipment",
            data=request_json,
            auth=requests.auth.HTTPBasicAuth(username, password),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"},
        )

        dhl_response.raise_for_status()

        response_json = dhl_response.json()
        base64_pdf: str = response_json["ShipmentResponse"]["LabelImage"][0]["GraphicImage"]
        encoded_label = base64.decodebytes(base64_pdf.encode("ascii"))

        s3_response = requests.post(
            f"https://dev.aws.com/s3/{s3_storage_bucket}",
            data=encoded_label,
            auth=requests.auth.HTTPBasicAuth(s3_username, s3_password),
            headers={"Content-Type": "application/octet-stream",
                     "Accept": "application/json"},
        )

        s3_response.raise_for_status()

        s3_response_json = s3_response.json()
        order.shipping_id = response_json["ShipmentResponse"]["ShippingId"]
        order.label_url = s3_response_json["Location"]
        order.save()
        return ("OK", 200)
    except Exception as e:
        print(e)
        raise e


def main():
    result = add_shipping("123")
    print(result)


if __name__ == "__main__":
    main()
