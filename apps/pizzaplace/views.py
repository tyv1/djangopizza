from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import get_resolver
from .models import Pizza
from .serializers import PizzaSerializer

class APIRoot(APIView):

    def get_url_patterns(self, url_dict, resolver, prefix=''):
        """
        Build a dicitonary of all URL patterns.
        """

        current_url = self.request.build_absolute_uri('/') # Get the current URL
        
        for pattern in resolver.url_patterns:
            if hasattr(pattern, 'url_patterns'):
                self.get_url_patterns(url_dict, pattern, prefix + pattern.pattern.regex.pattern)
            else:
                url = prefix + pattern.pattern.regex.pattern
                url = url.replace('^', '').replace('\\Z', '')
                if not url.startswith('api-auth') and not url.startswith('admin'):
                    url_dict[url] = current_url + url

    def get(self, request, format=None):
        """
        Return a dictionary of all endpoints in the API.
        """
        url_dict = {}
        resolver = get_resolver()
        self.get_url_patterns(url_dict, resolver)
        return Response(url_dict)


class PizzaView(APIView):
    def get(self, request):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)