from django.contrib.gis import admin
from .models import BusStops, EspooSmallRegions, EspooRegionalData, EspooPopulations

# Register your models here.
admin.site.register(BusStops, admin.OSMGeoAdmin)
admin.site.register(EspooSmallRegions, admin.OSMGeoAdmin)
admin.site.register(EspooRegionalData)
admin.site.register(EspooPopulations)
