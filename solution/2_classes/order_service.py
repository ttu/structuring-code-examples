from order_store import OrderStore
from dhl_client import DHLClient
from s3_client import S3Client


class OrderService(object):

    def __init__(self):
        self.order_store = OrderStore()
        self.dhl_client = DHLClient()
        self.s3_client = S3Client()

    def add_shipping_to_order(self, order_id: str) -> tuple[bool, str]:
        order = self.order_store.get_order(order_id)
        if not order:
            return (False, "Order")

        shipment_success, shipping_info = self.dhl_client.create_shipment_request(order)
        if not shipment_success:
            return (False, "Shipment")

        shipping_id = shipping_info[0]
        label_pdf = shipping_info[1]

        label_succes, label_url = self.s3_client.store_label(label_pdf)
        if not label_succes:
            return (False, "Label")

        self.order_store.update_order_shipping_label(order_id, shipping_id, label_url)

        return (True, "")
