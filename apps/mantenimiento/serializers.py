from rest_framework import serializers

from apps.auto.models import Auto

class AutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model: Auto