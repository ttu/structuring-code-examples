from order_service import add_shipping_to_order


def add_shipping(order_id: str):
    result = add_shipping_to_order(order_id)
    print("OK" if result[0] else "Error")


if __name__ == "__main__":
    order_id_input = "123"
    add_shipping(order_id_input)
