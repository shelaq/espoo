from django.contrib.gis import admin
from .models import BusStops, EspooSmallRegions, EspooRegionData

# Register your models here.
admin.site.register(BusStops, admin.OSMGeoAdmin)
admin.site.register(EspooSmallRegions, admin.OSMGeoAdmin)
admin.site.register(EspooRegionData)
