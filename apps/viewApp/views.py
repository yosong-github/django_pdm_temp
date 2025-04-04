from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.throttling import SimpleRateThrottle
from django.core.cache import cache as default_cache
from rest_framework.response import Response
from rest_framework import status

from apps.viewApp.serializer import AuthorSerializer
from apps.viewApp.models import Author

class MyThrottle(SimpleRateThrottle):
    scope = 'yosong'
    THROTTLE_RATES = {'yosong': '5/m'}
    cache = default_cache

    def get_cache_key(self, request, view):
        ident = 'yosong' + self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident,
        }

    def throttle_failure(self):
        raise APIException('你太快了')


class AuthorsView(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    throttle_classes = [MyThrottle, ]



    def throttled(self, request, wait):
        raise APIException('你太快了')
    # authentication_classes = []


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
