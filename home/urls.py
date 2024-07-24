
from django.contrib import admin
from django.urls import path
from . import views
from views import send_test_email

urlpatterns = [
    path('', views.index, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('subscribe_newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('send-test-email/', send_test_email, name='send_test_email'),
]