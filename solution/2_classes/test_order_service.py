from unittest.mock import patch

from order_service import OrderService


@patch('dhl_client.DHLClient.create_shipment_request', lambda self, x: (True, b"Mocked success"))
def test_add_shipping_to_order_shipment_success():
    orderId = "123"
    order_service = OrderService()

    result = order_service.add_shipping_to_order(orderId)
    assert result[0] is True, f"Expected True, got got {result[0]}"


@patch('dhl_client.DHLClient.create_shipment_request', lambda self, x: (False, "Mocked failure"))
def test_add_shipping_to_order_shipment_fail():
    orderId = "123"
    order_service = OrderService()

    result = order_service.add_shipping_to_order(orderId)
    assert result[0] is False, f"Expected False, got {result[0]}"
    assert result[1] == "Shipment", f"Expected Shipment, got {result[1]}"
