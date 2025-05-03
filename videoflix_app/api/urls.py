from django.urls import path, include
from auth_app.api.views import RegistrationView
from videoflix_app.api.views import VideoView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name="registerion"),
    path('videos/', VideoView.as_view(), name='videos')
]