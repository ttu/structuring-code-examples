from order_store import OrderStore
from dhl_client import DHLClient
from s3_client import send_label_to_s3

order_store = OrderStore()


def add_shipping_to_order(order_id: str) -> tuple[bool, str]:
    order = order_store.get_order(order_id)

    shipment_success, shipping_info = DHLClient.create_shipment_request(order)
    if not shipment_success:
        return (False, "Shipment")

    shipping_id = shipping_info[0]
    label_pdf = shipping_info[1]

    label_succes, label_url = send_label_to_s3(label_pdf)
    if not label_succes:
        return (False, "Label")

    order_store.update_order_shipping_label(order_id, shipping_id, label_url)
    return (True, "")
