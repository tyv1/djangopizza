from django.urls import path
from apps.pizzaplace.views import ToppingView, PizzaView

urlpatterns = [
    path('toppings/', ToppingView.as_view(), name='toppings'),
    path('pizzas/', PizzaView.as_view(), name='pizzas'),
]
