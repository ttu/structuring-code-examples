
def create_order_service(order_store, create_shipment_request, store_label):

    def add_shipping_to_order(order_id: str) -> tuple[bool, str]:
        order = order_store.get_order(order_id)
        if not order:
            return (False, "Order")

        shipment_success, shipping_info = create_shipment_request(order)
        if not shipment_success:
            return (False, "Shipment")

        shipping_id = shipping_info[0]
        label_pdf = shipping_info[1]

        label_succes, label_url = store_label(label_pdf)
        if not label_succes:
            return (False, "Label")

        order_store.update_order_shipping_label(order_id, shipping_id, label_url)
        return (True, "")

    # NOTE: Not in use, but kept as an example
    def get_order_shipping_label(order_id: str):
        order = order_store.get_order(order_id)

        if not order:
            return (False, "Order not found")
        if not order.label_url:
            return (False, "Order has no shipping label")

        return (True, order.label_url)

    return add_shipping_to_order, get_order_shipping_label
