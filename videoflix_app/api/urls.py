from django.urls import path, include
from videoflix_app.api.views import VideoView, SingleVideoView, server_staus

urlpatterns = [
    path('videos/', VideoView.as_view(), name='videos'),
    path('video/<int:video_id>/', SingleVideoView.as_view(), name='video-detail'),
    path('status/', server_staus, name='server-staus')
]