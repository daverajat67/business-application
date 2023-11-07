# businesses/views.py
from rest_framework import viewsets
from app.models import Business
from app.api.serializers import BusinessSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
