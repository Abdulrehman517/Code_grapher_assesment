from rest_framework import serializers, exceptions
from posts.models import Posts
from rest_framework.validators import UniqueValidator


class PostsIdRequiredSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def validate(self, attrs):
        id = attrs.get('id')
        post = Posts.objects.filter(id=id).first()
        if post is None:
            raise exceptions.ParseError('No post found')
        attrs['post'] = post
        return attrs


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = "__all__"

    def validate(self, attrs):
        name = attrs.get('title')
        if name == "":
            raise exceptions.ParseError('title required')

        return attrs
