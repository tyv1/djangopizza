from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pizza
from .serializers import PizzaSerializer


class PizzaView(APIView):
    def get(self, request):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)