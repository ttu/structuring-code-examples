from packages import Order


class OrderStore(object):

    def get_order(self, order_id: str):
        return Order.objects.filter(order_id=order_id).first()

    def update_order_shipping_label(self, order_id: str, shipping_id: str, label_url: str):
        order = self.get_order(order_id)
        order.shipping_id = shipping_id
        order.label_url = label_url
        order.save()
        return True
