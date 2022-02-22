from rest_framework import serializers
from counter.models import Count

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = '__all__'