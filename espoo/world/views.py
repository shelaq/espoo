from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EspooSmallRegions

# https://medium.com/crowdbotics/how-to-write-an-api-in-3-lines-of-code-with-django-rest-framework-59b0971edfa4
class EspooSmallRegionView(APIView):
 def get(self, request, pk=None):
     print(request.GET['coords'])
     # dog.feed()
     return Response ({'msg': 'Dog fed', 'status':status.HTTP_200_OK})
