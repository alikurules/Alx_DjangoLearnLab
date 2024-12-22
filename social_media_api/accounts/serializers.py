from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Fetch the custom user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for retrieving user details."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
# "serializers.CharField()", "get_user_model().objects.create_user"
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """Create a new user and generate an authentication token."""
        # Create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Generate a token for the new user
        Token.objects.create(user=user)
        return user
