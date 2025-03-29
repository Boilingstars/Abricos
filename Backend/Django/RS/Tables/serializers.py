from rest_framework import serializers
from models import Goods

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'username', 'email']