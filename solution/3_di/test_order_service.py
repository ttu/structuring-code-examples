from order_service import OrderService
from mocks import MockOrderStore, MockDHLClient, MockS3Client


def test_add_shipping_to_order_success():
    orderId = "123"
    order_service = OrderService(MockOrderStore(), MockDHLClient(), MockS3Client())

    result = order_service.add_shipping_to_order(orderId)
    assert result[0] is True, f"Expected True, got {result[0]}"


def test_add_shipping_to_order_label_fail():
    orderId = "123"
    order_service = OrderService(MockOrderStore(), MockDHLClient(), MockS3Client(False))

    result = order_service.add_shipping_to_order(orderId)
    assert result[0] is False, f"Expected False, got {result[0]}"
    assert result[1] == "Label", f"Expected Label, got {result[1]}"
