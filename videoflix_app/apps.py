from django.apps import AppConfig


class VideoflixAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videoflix_app'
    
    def ready(self):
        from .api import signals
