# Structuring Code

(WIP)

Examples how to structure code.

[example.py](example.py) contains a starting point

It has a single function / endpoint which will:
* Fetch order data from DB
* Create a shipment request for order to DHL API
* Store received lable binary to S3
* Update shipment id and label url to DB

DB / ORM and HTTP requests are faked in these examples. Fake implementations are in [external_packages.py](solution/external_packages.py).

### Getting stared

Install prerequisites
```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install flask
```

Execute example
```sh
export FLASK_APP=example && flask run
curl -X POST 127.0.0.1:5000/orders/123/shipping
```

### Example Solutions

0. Separated to functions
1. Separated to classes and modules
2. Separated to classes
3. Classes with Dependency injection
4. DI without classes

Run solutions, e.g. _solution/0_functions_/endpoint.py
```sh
export FLASK_APP=solution/0_functions/endpoint && flask run
curl -X POST 127.0.0.1:5000/orders/123/shipping
```
