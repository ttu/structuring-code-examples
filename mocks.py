
from dataclasses import dataclass
import json


class HttpAuth:
    def HTTPBasicAuth(self, *args):
        return self


class Response:
    def __init__(self, url):
        self.url = url

    def raise_for_status(self):
        pass

    def json(self):
        if 'dhl' in self.url:
            return json.loads('{ "ShipmentResponse": { "LabelImage": [ {"GraphicImage": "0000" } ] } }')
        if 'aws' in self.url:
            return json.loads('{ "Location": "http://some.url/images/dummy_id", "ShipmentResponse": { "ShippingId": "dummy_id" } }')

        raise Exception('Unknown url')


class requests:
    auth = HttpAuth()

    def post(url, data, auth, headers):
        return Response(url)


@dataclass
class QueryPayload:
    customer: any


@dataclass
class Customer:
    name: str
    address: str
    city: str


class QueryResponse:
    def __init__(self, order_id):
        self.order_id = order_id

    def first(self):
        customer = Customer('test', 'street 10', 'Helsinki')
        order = Order()
        order.order_id = self.order_id
        order.customer = customer
        return order


class Query:
    def __init__(self):
        self.filter = lambda order_id: QueryResponse(order_id)


class Order:
    objects = Query()
    shipping_id = ''
    label_url = ''
    customer= None

    def __init__(self):
        pass

    def save(self):
        pass
