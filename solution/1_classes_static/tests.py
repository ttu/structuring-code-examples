from unittest.mock import patch

from order_service import add_shipping_to_order


@patch('dhl_client.DHLClient.create_shipment_request', lambda x: (False, "Mocked failure"))
def test_add_shipping_to_order_shipment_fail():
    orderId = "123"
    result = add_shipping_to_order(orderId)
    assert result[0] is False, "Expected False, got %s" % result[0]
    assert result[1] is "Shipment", "Expected Shipment, got %s" % result[1]
