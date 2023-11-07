from django.db import models

# Create your models here.

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