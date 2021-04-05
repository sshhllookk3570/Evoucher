from django.contrib import admin
from django.urls import path
from Consumer import views

urlpatterns = [
    path("",views.show ),


]
