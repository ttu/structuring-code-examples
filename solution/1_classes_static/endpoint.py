from flask import Flask

from order_service import add_shipping_to_order

app = Flask(__name__)


@app.route('/orders/<order_id>/shipping', methods=['POST'])
def add_shipping(order_id: str):
    result = add_shipping_to_order(order_id)

    if (result[0]):
        return ("OK", 200)

    if result[1] == "Shipment":
        return ("Could not create shipment", 400)
    if result[1] == "Label":
        return ("Could not create label", 500)
    return ("Unknown error", 500)


def main():
    result = add_shipping("123")
    print(result)


if __name__ == "__main__":
    main()
