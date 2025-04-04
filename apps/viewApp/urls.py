from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from apps.viewApp.views import AuthorsView


router = DefaultRouter()
router.register('authors', AuthorsView, basename='authors')
urlpatterns = [
    path('', include(router.urls)),
]
