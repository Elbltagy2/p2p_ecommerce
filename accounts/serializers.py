from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    # We want the password to be write-only for security reasons
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Include password for registration
        extra_kwargs = {
            'password': {'write_only': True}  # Ensures the password is not included in the response
        }

    def create(self, validated_data):
        # Create a user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  # This will automatically hash the password
        )
        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    print (username,password)
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return {
                'access': str(refresh.access_token),  # Access token for authenticated user
                'refresh': str(refresh),              # Refresh token to get a new access token
            }
        raise serializers.ValidationError("Invalid credentials")