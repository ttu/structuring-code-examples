
import base64
import json
from typing import Optional

from flask import Flask

from packages import Order, requests


DHL_USERNAME = ""
DHL_PASSWORD = ""
S3_USERNAME = ""
S3_PASSWORD = ""
S3_STORAGE_BUCKET = ""

app = Flask(__name__)


@app.route('/orders/<order_id>/shipping', methods=['POST'])
def add_shipping(order_id: str):

    order = get_order(order_id)
    if not order:
        return ("Order not found", 404)

    shipment_success, shipping_info = create_shipment_request(order)
    if not shipment_success:
        return ("Shipment error", 400)

    shipping_id = shipping_info[0]
    label_pdf = shipping_info[1]

    label_succes, label_url = send_label_to_s3(label_pdf)
    if not label_succes:
        return ("Label error", 500)

    update_order_shipping_label(order_id, shipping_id, label_url)

    return ("OK", 200)


def create_shipment_request(order: Order):
    payload = json.dumps(parse_shipping_info(order))

    dhl_response = requests.post(
        "https://wsbexpress.dhl.com/rest/gbl/shipment",
        data=payload,
        auth=requests.auth.HTTPBasicAuth(DHL_USERNAME, DHL_PASSWORD),
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )

    if dhl_response.status_code != 200:
        return (False, None)

    response_json = dhl_response.json()

    base64_pdf: str = response_json["ShipmentResponse"]["LabelImage"][0]["GraphicImage"]
    encoded_label = base64.decodebytes(base64_pdf.encode("ascii"))
    return (True, (response_json["ShipmentResponse"]["ShippingId"], encoded_label))


def parse_shipping_info(order: Order):
    return {
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
        "reference": order.order_id,
    }


def send_label_to_s3(encoded_label: bytes):
    s3_response = requests.post(
        f"https://dev.aws.com/s3/{S3_STORAGE_BUCKET}",
        data=encoded_label,
        auth=requests.auth.HTTPBasicAuth(S3_USERNAME, S3_PASSWORD),
        headers={"Content-Type": "application/octet-stream", "Accept": "application/json"},
    )

    if s3_response.status_code != 200:
        return (False, "S3 error")

    s3_response_json = s3_response.json()
    return (True, s3_response_json["Location"])


def get_order(order_id: str) -> Optional[Order]:
    return Order.objects.filter(order_id=order_id).first()


def update_order_shipping_label(order_id: str, shipping_id: str, label_url: str):
    order = get_order(order_id)
    order.shipping_id = shipping_id
    order.label_url = label_url
    order.save()
    return True


def main():
    result = add_shipping("123")
    print(result)


if __name__ == "__main__":
    main()
