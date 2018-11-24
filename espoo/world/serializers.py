from rest_framework import serializers
from .models import EspooSmallRegions
class EspooSmallRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspooSmallRegions
        fields = ('kokotun', 'kunta', 'suur', 'tila', 'pien', 'nimi', 'nimi_iso', 'mtryhm', 'geom')
