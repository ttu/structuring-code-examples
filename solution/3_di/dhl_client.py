import base64
import json

from packages import requests


DHL_USERNAME = ""
DHL_PASSWORD = ""


class DHLClient:

    def create_shipment_request(self, order):
        payload = json.dumps(self._parse_shipping_info(order))

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

    def _parse_shipping_info(self, order):
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
