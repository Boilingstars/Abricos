from django.shortcuts import render
from rest_framework import generics
from Analytics.models import BuisnessMarketAnalysis
from Analytics.serializer import BuisnessMarketAnalysisSerializer

class BuisnessMarketAnalysisList(generics.ListAPIView):
    queryset = BuisnessMarketAnalysis.objects.all()
    serializer_class = BuisnessMarketAnalysisSerializer
