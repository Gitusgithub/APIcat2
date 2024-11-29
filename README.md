# E-Commerce Django Project

This project is a simple **E-Commerce application** built using the Django framework. It demonstrates how to define **one-to-many relationships** between models, manage database migrations, and set up a Django project for development and collaboration.

---

## **Features**

1. **Customer Model**
   - Stores customer details including:
     - `name`: Full name of the customer (string, up to 255 characters).
     - `email`: Unique email address (required, ensures no duplicates).

2. **Order Model**
   - Stores details of orders placed by customers:
     - `customer`: A foreign key linking the order to a specific customer.
     - `order_date`: The date and time when the order was placed (auto-filled).
     - `total_amount`: Total cost of the order, stored as a decimal value for accuracy.

3. **Data Relationships**
   - Each **Customer** can place multiple **Orders** (one-to-many relationship).
   - Orders are automatically deleted if the associated customer is removed (cascade behavior).

4. **Scalable Design**
   - The models are designed to be extended easily to include additional fields or features, such as customer addresses or order statuses.

---
