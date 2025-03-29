from django.contrib import admin
from django.urls import path, include
from .views import login_view

urlpatterns = [
    path('Login/', login_view, name='login'),
]