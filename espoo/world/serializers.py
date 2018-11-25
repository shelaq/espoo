from rest_framework import serializers
from .models import EspooPopulations
class EspooPopulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspooPopulations
        fields = ('district_id', 'year', 'total_population', 'moved_to_municipality', 'sisainen_in_migration', 'moved_from_municipality', 'sisainen_out_migration', 'total_net_migration')
