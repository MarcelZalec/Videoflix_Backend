from rest_framework import serializers
from auth_app.models import CustomUserModel


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUserModel
        fields = ['email','remember', 'provider', 'password', 'repeated_password']

    def validate(self, data):
        if data['password'] != data['repeated_password']:
            raise serializers.ValidationError({'error': 'Passwords do not match!'})
        
        if CustomUserModel.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'This email is already in use!'})
            
        return data
    
    def create(self, validated_data):
        validated_data.pop('repeated_password')
        user = CustomUserModel.objects.create_user(**validated_data)
        return user