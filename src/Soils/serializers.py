from rest_framework import serializers
from .models import Soil

class SoilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Soil
        fields = ('pk', 'lime_or_cement_stabilization', 'dose_of_lime_or_cement')