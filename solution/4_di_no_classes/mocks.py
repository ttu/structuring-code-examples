from dataclasses import dataclass

# pylint: disable=unused-argument


@dataclass
class MockOrder:
    id: str
    shipping_id: str
    label_url: str


class MockOrderStore:
    def __init__(self):
        self.order = MockOrder("", "", "")

    def get_order(self, order_id: str):
        self.order.id = order_id
        return self.order

    def update_order_shipping_label(self, order_id: str, shipping_id: str, label_url: str):
        self.order.shipping_id = shipping_id
        self.order.label_url = label_url
        return True


def mock_create_shipment_request(order):
    return True, ("1", bytes())


def mock_store_label(label_pdf: bytes):
    return True, "https://s3.amazonaws.com/mybucket/label.pdf"
