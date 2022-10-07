from unittest.mock import patch

# Note: will fail
# ModuleNotFoundError: No module named 'flask'
from api import add_shipping


@patch('endpoint.create_shipment_request', lambda x: (False, "Mocked failure"))
def test_add_shipping_to_order_shipment_fail():
    orderId = "123"
    result = add_shipping(orderId)
    assert result[0] is False, f"Expected False, got {result[0]}"
    assert result[1] == "Shipment", f"Expected Shipment, got {result[1]}"
