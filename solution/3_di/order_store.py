from packages import Order


class OrderStore:

    def get_order(self, order_id: str):
        return Order.objects.filter(order_id=order_id).first()

    def update_order_shipping_label(self, order_id: str, shipping_id: str, label_url: str):
        order = self.get_order(order_id)
        order.shipping_id = shipping_id
        order.label_url = label_url
        order.save()
        return True


# Use this class to show problems of not using base classes, e.g. forget to add required method
# Replace OrdereStore with ApiOrderStore from command.py
# AttributeError: 'ApiOrderStore' object has no attribute 'update_order_shipping_label'
class ApiOrderStore:

    def get_order(self, order_id: str):
        # We would fetch the order from the API in here
        # order = request.get(f"/api/orders/{order_id}")
        # return order
        return Order.objects.filter(order_id=order_id).first()

    # For example purposes, let's forget to add this method
    # def update_order_shipping_label(self, order_id: str, shipping_id: str, label_url: str):
        # pass
