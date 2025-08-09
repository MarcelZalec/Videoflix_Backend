from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed, NotAuthenticated

class VideoPermissons(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise NotAuthenticated({'error': 'Benutzer ist nicht authentifiziert.'})
        if request.method == 'GET':
            return True
        if request.method in ['PATCH', 'PUT', 'POST', 'DELETE'] and request.user.is_superuser:
            return True
        return False