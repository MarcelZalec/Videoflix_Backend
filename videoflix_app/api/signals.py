import os
from videoflix_app.models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from videoflix_app.tasks import *


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print(f"Video wurde geschpeichert {instance.video_file.path}")
    if created:
        file_path = instance.video_file.path
        convert_720p(file_path)
        convert_1080p(file_path)
        ## queue = django_rq.get_queue('default', autocommit=True)
        ## queue.enqueue(convert_240p, file_path)
        ## queue.enqueue(convert_480p, file_path)
        ## queue.enqueue(convert_720p, file_path)
        ## queue.enqueue(convert_1080p, file_path)


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding 'Video' object is deleted
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path + '_240p.mp4')
            os.remove(instance.video_file.path + '_480p.mp4')
            os.remove(instance.video_file.path + '_720p.mp4')
            os.remove(instance.video_file.path + '_1080p.mp4')