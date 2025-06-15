from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError("Email-Adresse ist erforderlich!")
        
        if username is None:  # Falls kein username übergeben wird, setze einen Default-Wert
            username = email
        
        extra_fields.setdefault('username', username)  # Optionales username-Handling
        user = self.model(email=email, **extra_fields)
        
        if password:
            user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, username, **extra_fields)