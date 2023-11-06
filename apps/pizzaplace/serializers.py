from rest_framework import serializers
from models import Pizza

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = [
            'id',
            'name',
            'description',
            'price',
            'image'
            ]