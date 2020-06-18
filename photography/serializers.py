from .models import Photography
from rest_framework import serializers


class PhotographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Photography
        fields = '__all__'
        depth = 1