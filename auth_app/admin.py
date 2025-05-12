from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel, PasswordReset

# Register your models here.

admin.site.register(CustomUserModel, UserAdmin)
admin.site.register(PasswordReset)