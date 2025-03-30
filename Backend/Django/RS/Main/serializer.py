from rest_framework import serializers
from Main.models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'