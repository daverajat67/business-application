from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
   
    path('', views.bussiness_crud, name="business_list"),
    path('update/<int:pk>', views.update_bussiness, name="business_update"),
    path('delete/<int:pk>', views.delete_business, name="business_delete"),


    

]