from abc import abstractmethod, ABC, ABCMeta
from packages import Order


class StoreBase(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_order(self, order_id: str) -> Order:
        raise NotImplementedError

    @abstractmethod
    def update_order_shipping_label(self, order_id: str, shipping_id: str, label_url: str) -> bool:
        raise NotImplementedError


class OrderStore(StoreBase):
    def get_order(self, order_id: str) -> Order:
        return Order.objects.filter(order_id=order_id).first()

    def update_order_shipping_label(self, order_id: str, shipping_id: str, label_url: str) -> bool:
        order = self.get_order(order_id)
        order.shipping_id = shipping_id
        order.label_url = label_url
        order.save()
        return True


# Replace OrdereStore with ApiOrderStore from command.py
# TypeError: Can't instantiate abstract class ApiOrderStore with abstract method update_order_shipping_label
class ApiOrderStore(StoreBase):
    def get_order(self, order_id: str) -> Order:
        # We would fetch the order from the API in here
        # order = request.get(f"/api/orders/{order_id}")
        # return order
        return Order.objects.filter(order_id=order_id).first()

    # For example purposes, let's forget to add this method
    # def update_order_shipping_label(self, order_id: str, shipping_id: str, label_url: str) -> bool:
    #     pass
