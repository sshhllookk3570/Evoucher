from django.contrib import admin
from django.urls import path
from Admin import views

app_name = 'Admin'
urlpatterns = [
    path("", views.index,),
    path("show/", views.showvoucher,name='show'),
    path("assign/", views.assign_code,name='assign'),
   # path("consumerform/", views.assign_code, name='assign_code'),

]
