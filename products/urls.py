
#from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update-review/<int:pk>/', views.update_review, name='update_review_form'),
    path('delete-review/<int:pk>/', views.delete_review, name='delete_review_form'),
]