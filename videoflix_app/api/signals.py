import os
import shutil
from videoflix_app.models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from videoflix_app.tasks import *
from django_rq import job, get_queue

import logging


logger = logging.getLogger(__name__)

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        queue = get_queue('default', autocommit=True)       
        try:
            job = queue.enqueue(process_video, instance)
            logger.debug(f"Job successfully enqueued: {job.id}")
        except Exception as e:
                logger.error(f"Error enqueuing job: {str(e)}")


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding 'Video' object is deleted
    """
    folder_path = os.path.dirname(instance.video_file.path)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    # if instance.video_file:
    #     if os.path.isfile(instance.video_file.path):
    #         path = remove_mp4_from_string(instance.video_file.path)
    #         
    #         os.remove(path + '_720p.mp4')
    #         os.remove(path + '_1080p.mp4')