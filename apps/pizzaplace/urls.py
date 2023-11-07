from django.urls import path, include
from .views import APIRoot
from apps.pizzaplace.views import PizzaView

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('pizzas/', PizzaView.as_view(), name='pizzas'),
]
