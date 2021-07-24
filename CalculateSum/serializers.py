from rest_framework import serializers
from .models import CalculateSum


class CalculateSumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculateSum
        fields = '__all__'
