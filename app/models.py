from django.db import models

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=100)
    address= models.CharField(max_length=500)
    owner_info = models.CharField(max_length=300)
    employee_size = models.IntegerField()
 