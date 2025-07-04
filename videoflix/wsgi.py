"""
WSGI config for videoflix project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from videoflix.settings_loader import settings_module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module())

application = get_wsgi_application()
