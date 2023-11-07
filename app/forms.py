from django import forms
from app.models import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = "__all__"