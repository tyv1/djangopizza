from django.urls import path
from .views import PizzaView


urlpatterns = [
    path('pizzas/', PizzaView.as_view()),
]