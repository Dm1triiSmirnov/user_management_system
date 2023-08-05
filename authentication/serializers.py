from users.models import CustomUser
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        """
        Validate the password and password2 fields.
        """
        password = data.get('password')
        password2 = data.get('password2')
        if password and password2 and password != password2:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        """
        Create and return a new user.
        """
        del validated_data['password2']
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
