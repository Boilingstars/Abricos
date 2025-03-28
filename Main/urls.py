from django.contrib import admin
from django.urls import path, include
from Main import views

urlpatterns = [
    path('interface/', views.index, name='home')
]