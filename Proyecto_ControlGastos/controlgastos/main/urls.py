from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("inicio", views.home_main),
path('createuser', views.create_users_main),
path('listusers', views.list_users_main),
path('updateuser', views.update_users_main)
]