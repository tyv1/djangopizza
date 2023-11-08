from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Topping, Pizza
from .serializers import ToppingSerializer, PizzaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ToppingView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        toppings = Topping.objects.all()
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PizzaView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    