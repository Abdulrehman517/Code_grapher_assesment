

from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.Serializers.SignupSerializers import AddUserSerializer

class SignUpView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        user = AddUserSerializer(data=request.data)
        if user.is_valid(raise_exception=True):
            user.save()
            return Response({"detail": "User created"}, status=201)
        else:
            return Response(user.errors, status=422)