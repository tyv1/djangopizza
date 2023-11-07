from rest_framework import serializers
from .models import Topping, Pizza

class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topping
        fields = [
            'id',
            'name'
            ]

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = [
            'id',
            'name',
            'toppings',
            'description',
            'price',
            'image'
            ]