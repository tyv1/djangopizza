from django.urls import path
from .api_views import PizzaView


urlpatterns = [
    path('pizzas/', PizzaView.as_view()),
]