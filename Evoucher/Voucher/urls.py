from django.contrib import admin
from django.urls import path
from Voucher import views

urlpatterns = [
    path("", views.get_data ,name='form'),


]
