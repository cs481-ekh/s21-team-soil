from rest_framework import serializers
from .models import soil_sample

class soilserializer(serializers.ModelSerializer):

    class Meta:
        model = soil_sample
        fields = ('pk', 'lime_or_cement_stabilization', 'dose_of_lime_or_cement')