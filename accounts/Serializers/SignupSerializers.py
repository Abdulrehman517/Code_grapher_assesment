
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import User


class AddUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])


    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "password")

    def validate(self, data):
        username = data.get('username')
        email = data.get("email")
        if '@' not in email:
            raise serializers.ValidationError({"Email": "Invalid email, Please include @."})
        if ' ' in username:
            raise serializers.ValidationError({"username": "Spaces cannot be in username"})
        return data

    def create(self, validated_data):
        checkUser = User.objects.filter(username=validated_data.get("username")).first()
        if checkUser is not None:
            raise serializers.ValidationError({"detail": "Username already exist"})
        else:
            user = User.objects.create(
                first_name=validated_data.get("first_name"),
                last_name=validated_data.get("last_name"),
                username=validated_data.get("username"),
                email=validated_data.get("email"),
            )

            user.set_password(validated_data.get("password"))
            user.save()
            return user

