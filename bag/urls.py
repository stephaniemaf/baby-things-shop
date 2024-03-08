
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_bag, name='shop_bag'),
    path('add/<item_id>', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>', views.adjust_bag, name='adjust_bag'),
    path('remove/<int:item_id>/', views.remove_from_bag, name='remove_from_bag'),
    ]