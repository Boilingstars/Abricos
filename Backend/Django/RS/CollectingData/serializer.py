from rest_framework import serializers
from CollectingData.models import CollectedData

class CollectingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedData
        fields = '__all__'