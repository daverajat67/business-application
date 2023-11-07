# businesses/serializers.py
from rest_framework import serializers
from app.models import Business

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
