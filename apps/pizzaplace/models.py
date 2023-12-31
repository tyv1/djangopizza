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
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

# TODO: add functionality for ordering multiple/customizing
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    modification = models.ManyToManyField(Topping, through='OrderItemModification')

class OrderItemModification(models.Model):
    MODIFICATIONS = [
        ('None', 'None'),
        ('Extra', 'Extra'),
        ('Remove', 'Remove'),
    ]

    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    modification = models.CharField(max_length=10, choices=MODIFICATIONS, default='None')