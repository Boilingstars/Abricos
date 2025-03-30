from rest_framework import serializers
from Analytics.models import BuisnessMarketAnalysis

class BuisnessMarketAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuisnessMarketAnalysis
        fields = '__all__'