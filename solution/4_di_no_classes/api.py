from flask import Flask

from order_service import create_order_service
from order_store import OrderStore
from dhl_client import DHLClient
from s3_client import S3Client


app = Flask(__name__)


add_shipping_to_order, get_shipping_label = create_order_service(
    OrderStore(),
    lambda x: DHLClient().create_shipment_request(x),
    lambda x: S3Client().store_label(x))


@app.route('/orders/<order_id>/shipping', methods=['POST'])
def add_shipping(order_id: str):
    result = add_shipping_to_order(order_id)

    if (result[0]):
        return ("OK", 200)

    if result[1] == "Order":
        return ("Order not found", 404)
    if result[1] == "Shipment":
        return ("Could not create shipment", 400)
    if result[1] == "Label":
        return ("Could not create label", 500)
    return ("Unknown error", 500)
