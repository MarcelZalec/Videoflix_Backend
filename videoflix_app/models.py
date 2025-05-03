from django.db import models
from datetime import datetime
from auth_app.models import CustomUserModel
import re

# Create your models here.
def clean_filename(title):
    return re.sub(r'[^a-zA-Z0-9_]+', '_', title)

def video_file_path(instance, filename):
    title = clean_filename(instance.title)
    title = title[:50]  
    folder_path = f'videos/{title}' 
    return f'{folder_path}/{filename}' 

class Video(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)
    video_file = models.FileField(upload_to='videos', blank=True, null=True)
    thumbnail = models.ImageField(upload_to=video_file_path, blank=True, null=True)
    
    def __str__(self):
        return self.title

class UserFavoriteVideo(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
class UserContinueWatchVideo(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)