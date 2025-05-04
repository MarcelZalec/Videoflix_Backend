from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import *


class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        data = {}
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email
            }
        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_200_OK)


class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user = saved_account)
            print(f"Das ist der accsess Token {token}")
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email
            }
            saved_account.is_active = True
        else:
            data = serializer.errors
            return Response({'error': 'Etwas ist schiefgelaufen'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data, status=status.HTTP_201_CREATED)