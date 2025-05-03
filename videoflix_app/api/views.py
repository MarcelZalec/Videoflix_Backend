from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from videoflix_app.models import Video
from rest_framework.permissions import AllowAny


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# @cache_page(CACHE_TTL)
class VideoView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        serializer = VideoSerializer(data = request.data)
        serializer.is_valid()
        data = Video.objects.all()
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'test': 'das ist ein test'})