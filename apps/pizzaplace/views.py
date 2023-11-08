from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Topping, Pizza, Store, Customer, Order
from .serializers import ToppingSerializer, PizzaSerializer, StoreSerializer, CustomerSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated


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

class StoreView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

class CustomerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)