from django.urls import path
from .views import PizzaView


urlpatterns = [
    path('', PizzaView.as_view()),
]