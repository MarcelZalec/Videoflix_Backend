import os
from auth_app.models import CustomUserModel
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator as PRTG
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.urls import reverse
import django_rq

from rest_framework.response import Response


@receiver(post_save, sender=CustomUserModel)
def user_post_create(sender, instance, created, **kwargs):
    pass
    if created and not instance.is_active:
        tg = PRTG()
        token = tg.make_token(instance)
        uid = urlsafe_base64_encode(force_bytes(instance.pk))
        activation_url = reverse('activate_user', kwargs={'uidb64': uid, 'token': token})
        full_url = f'{settings.FRONT_END}{activation_url}'
        domain_url = "http://localhost:5500/" #os.getenv('REDIRECT_LANDING')
        text_content = render_to_string(
            "emails/activation_email.txt",
            context={'user': instance, 'activation_url': full_url, 'domain_url': domain_url},
        )
        html_content = render_to_string(
            "emails/activation_email.html",
            context={'user': instance, 'activation_url': full_url, 'domain_url': domain_url},
        )
        subject = 'Confirm your email'
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=True)