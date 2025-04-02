from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class ErrorMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        print(exception)
        return HttpResponse('啊吧啊吧')
