from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.Serializers.SigninSerializers import UserSerializer
from accounts.models import User


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        id = request.GET.get('id')
        if id is not None:
            user = User.objects.filter(id=id).first()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            posts = User.objects.all()
            serializer = UserSerializer(posts, many=True)
            return Response(serializer.data)

