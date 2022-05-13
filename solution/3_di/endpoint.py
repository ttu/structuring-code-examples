from dataclasses import dataclass
from order_service import OrderService

# in this example we don't have reference to real ORM data model
# so we need to create a model for it
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


class MockDHLClient(object):
    def create_shipment_request(self, order):
        return True, ("1", bytes())


class MockS3Client(object):
    def send_label_to_s3(self, label_pdf: bytes):
        return True, "https://s3.amazonaws.com/mybucket/label.pdf"


store = MockOrderStore()

order_service = OrderService(MockOrderStore(), MockDHLClient(), MockS3Client())


def post_endpoint(req: any):
    order_id = req["order_id"]
    result = order_service.add_shipping_to_order(order_id)

    if (result[0]):
        return 200

    if result[1] == "Shipment":
        return 400, "Could not create shipment"
    if result[1] == "Label":
        return 500, "Could not create label"
    return 500, "Unknown error"


def main():
    result = post_endpoint({"order_id": "123"})
    print(result)


if __name__ == "__main__":
    main()
