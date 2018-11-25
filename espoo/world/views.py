from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EspooSmallRegions
from django.contrib.gis.geos import GEOSGeometry, Point

# https://medium.com/crowdbotics/how-to-write-an-api-in-3-lines-of-code-with-django-rest-framework-59b0971edfa4
class EspooSmallRegionView(APIView):
 def get(self, request, pk=None):
     print(request.GET['lon'], request.GET['lat'])
     print(type(request.GET['lon']))
     print('--')
     pnt = Point(float(request.GET['lon']),float(request.GET['lat']))
     reponse = 'oops'
     try:
         reg = EspooSmallRegions.objects.get(geom__intersects=pnt)
         if reg:
             reponse = region.district_id
     except Exception:
         print('oops')

     # "POINT (Lon Lat)"
     # dog.feed()

     return Response ({'msg': response, 'status':status.HTTP_200_OK})
