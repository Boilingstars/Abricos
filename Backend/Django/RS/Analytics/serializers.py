from rest_framework import serializers
from models import Stats

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ['id', 'username', 'email']