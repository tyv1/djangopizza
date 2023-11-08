from django.db import models
from django.contrib.auth.models import User

class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    toppings = models.ManyToManyField(Topping)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='pizza_images', blank=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# A pizza order is a pizza with a set of toppings and a quantity
class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order = models.ForeignKey('OrderDetails', on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.pizza.name}"


# An order details is a set of pizza orders
class OrderDetails(models.Model):
    pizzas = models.ManyToManyField(Pizza, through='PizzaOrder', related_name='order_details')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {', '.join([str(pizza_order) for pizza_order in self.pizzaorder_set.all()])}"


# An order is a set of order details and other relevant information
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    fulfilled = models.BooleanField(default=False)