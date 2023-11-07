from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import get_resolver


class APIRoot(APIView):
    def get_url_patterns(self, url_list, resolver, prefix=''):
        """
        Recursively build a list of all URL patterns in the resolver tree.
        """
        for pattern in resolver.url_patterns:
            if hasattr(pattern, 'url_patterns'):
                self.get_url_patterns(url_list, pattern, prefix + pattern.pattern.regex.pattern)
            else:
                url = prefix + pattern.pattern.regex.pattern
                url = url.replace('^', '').replace('\\Z', '')
                if not url.startswith('api-auth') and not url.startswith('admin'):
                    url_list.append(url)

    def get(self, request, format=None):
        """
        Return a list of all endpoints in the API.
        """
        url_list = []
        resolver = get_resolver()
        self.get_url_patterns(url_list, resolver)
        return Response(url_list)