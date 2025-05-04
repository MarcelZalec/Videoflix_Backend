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
    
    def get(self, request, format=None):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VideoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @cache_page(CACHE_TTL)
class SingleVideoView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, video_id):
        video = Video.objects.get(pk = video_id)
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, video_id):
        video = Video.objects.get(pk = video_id)
        serializer = VideoSerializer(video)
        video.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, video_id):
        video = Video.objects.get(pk = video_id)
        serializer = VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)