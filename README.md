# Structuring Code

(WIP)

Examples how to structure code 

[example.py](example.py) contains a starting point

It has a single function which will
* Fetch order data from DB
* Create a shipment request for order
* Store received lable binary to S3
* Update shipment id and label url to DB

### Solutions

0. Separated to functions
1. Separated to classes and modules
2. Separated to classes
3. Classes with Dependency injection
4. DI without classes