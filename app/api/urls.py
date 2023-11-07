# businesses/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import BusinessViewSet

router = DefaultRouter()
router.register('businesses', BusinessViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
