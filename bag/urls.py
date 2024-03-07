
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_bag, name='shop_bag'),
     path('add/<item_id>', views.add_to_bag, name='add_to_bag')
    ]