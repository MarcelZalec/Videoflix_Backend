from django.urls import path, include
from auth_app.api.views import RegistrationView, LoginView, RequestPassowrdResetView
from videoflix_app.api.views import VideoView, SingleVideoView
from videoflix_app.functions import activate_user

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registerion'),
    path('login/', LoginView.as_view(), name='login'),
    path('resetPass/', RequestPassowrdResetView.as_view(), name='reset_password'),
    path('resetPass/<token>', RequestPassowrdResetView.as_view(), name='reset_password_token'),
    path('videos/', VideoView.as_view(), name='videos'),
    path('video/<int:video_id>/', SingleVideoView.as_view(), name='video-detail'),
    path('activate/<uidb64>/<token>/', activate_user, name='activate_user'),
]