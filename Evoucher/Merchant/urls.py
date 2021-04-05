from django.contrib import admin
from django.urls import path
from Merchant import views

urlpatterns = [
    path("",views.redeem ),


]
