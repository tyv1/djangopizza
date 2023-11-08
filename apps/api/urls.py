from django.urls import path, include
from .views import APIRoot

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('', include('apps.pizzaplace.urls')),
]