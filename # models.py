# models.py
from django.db import models

class Customer(models.Model):
    """
    Represents a customer in the e-commerce system.
    Fields:
        - name: The name of the customer (string, max length 255).
        - email: The email address of the customer (must be unique).
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name  # Display the customer's name in admin and queries.


class Order(models.Model):
    """
    Represents an order placed by a customer.
    Fields:
        - customer: A reference to the Customer who placed the order (foreign key).
        - order_date: The date and time when the order was created (auto-generated).
        - total_amount: The total amount for the order (decimal with 2 places).
    """
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,  # Delete all orders if the customer is deleted.
        related_name='orders'      # Allows reverse access (e.g., customer.orders.all()).
    )
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"