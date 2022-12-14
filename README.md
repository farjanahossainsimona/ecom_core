# This description include the overall idea of the project and this is for learning purpose. 

This is a ecommerce site.

* This project will be designed by monolithic architechture.
* There should be several independent component. And the asyncronous communication between the servicees will be held by `Event driven architecture`.

### Services:

* **ecom_core**: This will be the main app of this project.
  * User authentication, authorization and role management.
  * A webhook machanism should be implemented for `Event driven architecture`
* **ecom_business**: This app should contain the business logic of `cart`, `order`, `product`, `vouchers` and the other calculations.
* **ecom_payment**: This app should contain the online payament system for a order.
* **ecom_report**: This app should contain the report generation part.

