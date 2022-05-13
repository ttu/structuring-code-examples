from dataclasses import dataclass
from flask import Flask

from order_service import create_order_service
from order_store import OrderStore
from dhl_client import DHLClient
from s3_client import S3Client


@dataclass
class Order:
    id: str
    shipping_id: str
    label_url: str


class MockOrderStore:
    def __init__(self):
        self.order = Order("", "", "")

    def get_order(self, order_id: str):
        self.order.id = order_id
        return self.order

    def update_order_shipping_label(self, order_id: str, shipping_id: str, label_url: str):
        self.order.shipping_id = shipping_id
        self.order.label_url = label_url
        return True


def mock_create_shipment_request(order):
    return True, ("1", bytes())


def mock_send_label_to_s3(label_pdf: bytes):
    return True, "https://s3.amazonaws.com/mybucket/label.pdf"


# add_shipping_to_order = create_order_service(MockOrderStore(), mock_create_shipment_request, mock_send_label_to_s3)
add_shipping_to_order = create_order_service(
    OrderStore(),
    lambda x: DHLClient().create_shipment_request(x),
    lambda x: S3Client().send_label_to_s3(x))


app = Flask(__name__)


@app.route('/orders/<order_id>/shipping', methods=['POST'])
def add_shipping(order_id: str):
    result = add_shipping_to_order(order_id)

    if (result[0]):
        return ("OK", 200)

    if result[1] == "Shipment":
        return ("Could not create shipment", 400)
    if result[1] == "Label":
        return ("Could not create label", 500)
    return ("Unknown error", 500)


def main():
    result = add_shipping("123")
    print(result)


if __name__ == "__main__":
    main()
