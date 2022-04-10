from order_service import OrderService

order_service = OrderService()

def post_edpoint(req: any):
    order_id = req["order_id"]
    result = order_service.add_shipping_to_order(order_id)
    
    if (result[0]):
        return 200

    if result[1] == "Shipment":
        return 400, "Could not create shipment"
    if result[1] == "Label":
        return 500, "Could not create label"
    return 500, "Unknown error"

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()