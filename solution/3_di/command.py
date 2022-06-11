from order_service import OrderService
from order_store import OrderStore
from dhl_client import DHLClient
from s3_client import S3Client


order_service = OrderService(OrderStore(), DHLClient(), S3Client())


def add_shipping(order_id: str):
    result = order_service.add_shipping_to_order(order_id)
    print("OK" if result[0] else "Error")


if __name__ == "__main__":
    order_id = "123"
    add_shipping(order_id)
