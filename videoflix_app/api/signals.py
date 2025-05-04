import os
from videoflix_app.models import Video
from auth_app.models import CustomUserModel
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save
from videoflix_app.tasks import *

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as tg
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.urls import reverse


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde geschpeichert")
    if created:
        convert_240p(instance.video_file.path)
        convert_480p(instance.video_file.path)
        convert_720p(instance.video_file.path)
        convert_1080p(instance.video_file.path)


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


@receiver(post_save, sender=CustomUserModel)
def user_post_create(sender, instance, created, **kwargs):
    pass
#    if created and not instance.is_active:
#        token = tg.make_token(instance)
#        uid = urlsafe_base64_encode(force_bytes(instance.pk))
#        activation_url = reverse('activate_user', kwargs={'uidb64': uid, 'token': token})
#        full_url = f'{settings.DOMAIN_NAME}{activation_url}'
#        domain_url = os.getenv('REDIRECT_LANDING')
#        text_content = render_to_string(
#            "emails/activation_email.txt",
#            context={'user': instance, 'activation_url': full_url, 'domain_url': domain_url},
#        )
#        html_content = render_to_string(
#            "emails/activation_email.html",
#            context={'user': instance, 'activation_url': full_url, 'domain_url': domain_url},
#        )
#        subject = 'Confirm your email'
#        msg = EmailMultiAlternatives(
#            subject,
#            text_content,
#            settings.DEFAULT_FROM_EMAIL,
#            [instance.email],
#        )
#        msg.attach_alternative(html_content, "text/html")
#        msg.send()