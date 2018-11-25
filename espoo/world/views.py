from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EspooSmallRegions, BusStops, EspooRegionalData, EspooPopulations
from .serializers import EspooPopulationsSerializer
from django.core import serializers
from django.contrib.gis.geos import Point

# https://medium.com/crowdbotics/how-to-write-an-api-in-3-lines-of-code-with-django-rest-framework-59b0971edfa4
class EspooSmallRegionView(APIView):
 def get(self, request, pk=None):
     print(request.GET['lon'], request.GET['lat'], request.GET['year'])
     print(type(request.GET['lon']))
     pnt = Point(float(request.GET['lon']),float(request.GET['lat']))
     # try:
     region = EspooSmallRegions.objects.get(geom__contains=pnt)
     bus_stops = BusStops.objects.filter(mpoly__distance_lte=(pnt, 500))

     district_id = region.pien
     year = request.GET['year']


     population_stats = EspooPopulations.objects.filter(district_id = district_id, year=year)
     # population_out = EspooPopulationsSerializer(population_stats,many=True)

     languages = EspooRegionalData.objects.filter(district_id = district_id, year=year)
     return Response ({
     'population_stats': serializers.serialize('json', population_stats),
     'languages': serializers.serialize('json', languages),
     'bus_stops': serializers.serialize('json', bus_stops),
     'status':status.HTTP_200_OK
     })
     # except Exception:
     #     return Response ({'msg': 'Did not click in an Espoo region', 'status':400})

     # "POINT (Lon Lat)"
     # dog.feed()
