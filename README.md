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
python -m pip install -e .
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
5. Classes and base classes

Run solutions, e.g. _solution/0_functions_/api.py
```sh
export FLASK_APP=solution/0_functions/api && flask run
curl -X POST 127.0.0.1:5000/orders/123/shipping
```

Run command, e.g. _solution/4_di_no_classes/command.py_
```sh
python solution/4_di_no_classes/command.py
```

Run tests, e.g. _solution/4_di_no_classes/test_order_service.py_
```sh
pytest solution/4_di_no_classes/test_order_service.py
```

NOTE: To execute tests with VS Code, open each solution directory separately in VS Code.

Each solution has the separation implemented in a different way, but each solution has separation to 3 "layers".

1. Entrypoint (API / Command)
2. Business logic
3. DB/API connection

## 0. Separated to functions
* For readability, move functionality to separate functions
* We can test functionality with patching (fails as the module has reference to Flask)

## 1. Separated to classes and modules
* For readability, move functions to separate classes and modules
  * Classes are stateless (static), so from the functional perspective classes are just modules
* Testing with patching

## 2. Separated to classes
* Move functionality to classes
* Service has high coupling, as it creates all instances, so not real benefit over previous solution.
* Testign with patching.

## 3. Classes with Dependency injection
* Inject dependencies into service.
* No need to use base classes as Python supports duck typing. Makes code more understandable, if we use base classes and reduces errors.

## 4. DI without classes
* Example how to use DI without classes.
* Understandability is reduced, but it is possible to use DI without classes.

## 5. DI with classes and base classes
* Example of using base class with OrderStore