from order_service import add_shipping_to_order

@POST
def post_edpoint(req: any):
    order_id = req["order_id"]
    result = add_shipping_to_order(order_id)
    
    if (result[0]):
        return 200

    if result[1] == "Shipment":
        return 400, "Could not create shipment"
    if result[1] == "Label":
        return 500, "Could not create label"
    return 500, "Unknown error"