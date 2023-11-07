from django.urls import path, include
from .views import APIRoot

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('pizzas/', include('apps.pizzaplace.urls'), name='pizzas'),
]
