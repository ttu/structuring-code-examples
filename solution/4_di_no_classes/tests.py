import re
from order_service import create_order_service
from mocks import MockOrderStore, mock_create_shipment_request, mock_store_label


def test_add_shipping_to_order_success():
    orderId = "123"
    add_shipping_to_order = create_order_service(MockOrderStore(), mock_create_shipment_request, mock_store_label)

    result = add_shipping_to_order(orderId)
    assert result[0] is True, "Expected True, got %s" % result[0]


def test_add_shipping_to_order_label_fail():
    orderId = "123"
    add_shipping_to_order = create_order_service(
        MockOrderStore(), mock_create_shipment_request, lambda x: (False, "S3 failed"))

    result = add_shipping_to_order(orderId)
    assert result[0] is False, "Expected False, got %s" % result[0]
    assert result[1] == "Label", "Expected Label, got %s" % result[1]
