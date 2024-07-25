
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_bag, name='shop_bag'),
    path('add_and_remove/<item_id>/', views.add_and_remove, name='add_and_remove'),
    path('adjust/<int:item_id>/', views.adjust_bag, name='adjust_bag'),
    path('bag/empty/', views.empty_bag, name='empty_bag'),
    path('apply_discount/', views.apply_discount, name='apply_discount'),
    

    ]