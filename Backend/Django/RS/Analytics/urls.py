from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('Analytics/', views.BuisnessMarketAnalysisList.as_view(), name='buisness_market_nalysis-list'),
]