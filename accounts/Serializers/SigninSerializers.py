from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions

from rest_framework.exceptions import APIException

from accounts.models import User


class ServiceUnavailable(exceptions.ValidationError):
    status_code = 401


class LoginSerializer(serializers.Serializer):
    usernameOrEmail = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("usernameOrEmail", "")
        password = data.get("password", "")
        if username and password:
            if "@" in username:
                try:
                    fetchUser = User.objects.get(email=username)
                    username = fetchUser.username
                except User.DoesNotExist:
                    raise exceptions.ValidationError({"detail": "Invalid email"})
            user = authenticate(username=username, password=password)
            if user is not None:
                data["user"] = user
            else:

                msg = {"detail": "Invalid credentials"}
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both"
            raise exceptions.ParseError(msg)

        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'