from dataclasses import dataclass


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


class MockDHLClient(object):
    def create_shipment_request(self, order):
        return True, ("1", bytes())


class MockS3Client(object):
    def __init__(self, success=True):
        self.success = success

    def store_label(self, label_pdf: bytes):
        return self.success, "https://s3.amazonaws.com/mybucket/label.pdf"
