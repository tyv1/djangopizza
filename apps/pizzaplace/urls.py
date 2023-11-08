from django.urls import path
from apps.pizzaplace.views import ToppingView, PizzaView, StoreView, CustomerView, OrderView

urlpatterns = [
    path('toppings/', ToppingView.as_view(), name='toppings'),
    path('pizzas/', PizzaView.as_view(), name='pizzas'),
    path('stores/', StoreView.as_view(), name='stores'),
    path('customers/', CustomerView.as_view(), name='customers'),
    path('orders/', OrderView.as_view(), name='orders'),
]
