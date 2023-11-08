from django.contrib import admin
from .models import Topping, Pizza, Store, Customer, Order

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Store)
admin.site.register(Customer)
admin.site.register(Order)
