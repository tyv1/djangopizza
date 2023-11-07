from django.urls import path, include
from .views import APIRoot
from apps.pizzaplace.views import ToppingView, PizzaView

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('toppings/', ToppingView.as_view(), name='toppings'),
    path('pizzas/', PizzaView.as_view(), name='pizzas'),
]
