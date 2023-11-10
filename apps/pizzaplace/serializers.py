from rest_framework import serializers
from .models import Topping, Pizza, Store, Customer, Order

class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topping
        fields = [
            'id',
            'name'
            ]

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    toppings = ToppingSerializer(many=True)

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

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = [
            'id',
            'name',
            'address',
            'phone'
            ]

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'user',
            'phone',
            'address',
            'store'
            ]

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'store',
            'items',
            'order_date',
            ]
        