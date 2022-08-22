from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Posts
from posts.Serializers.PostsSerializers import PostsIdRequiredSerializer, PostSerializer


class PostListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        id = request.GET.get('id')
        if id is not None:
            serializer = PostsIdRequiredSerializer(data=request.GET)
            serializer.is_valid(raise_exception=True)
            serializer = PostSerializer(serializer.validated_data['post'])
            return Response(serializer.data)
        else:
            posts = Posts.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)


class PostsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeletePostAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def put(self, request):
        serializer = PostsIdRequiredSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ser = PostSerializer(data=request.data, instance=serializer.validated_data['post'])
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def delete(self, request):
        serializer = PostsIdRequiredSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['post'].delete()
        return Response(serializer.data)