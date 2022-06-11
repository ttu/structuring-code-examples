from order_service import create_order_service
from order_store import OrderStore
from dhl_client import DHLClient
from s3_client import S3Client


add_shipping_to_order = create_order_service(
    OrderStore(),
    lambda x: DHLClient().create_shipment_request(x),
    lambda x: S3Client().store_label(x))


def add_shipping(order_id: str):
    result = add_shipping_to_order(order_id)
    print("OK" if result[0] else "Error")


if __name__ == "__main__":
    order_id = "123"
    add_shipping(order_id)
