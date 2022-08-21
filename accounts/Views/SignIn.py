# from rest_framework.response import Response
# from rest_framework.views import APIView
# from accounts.Serializers.SigninSerializers import LoginSerializer, UserSerializer
# from accounts.models import  User
# import datetime
#
#
# class SignIn(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data["user"]
#             token, created = Token.objects.get_or_create(user=user)
#             last_token = None
#             if not created:
#                 if user.username == "alchemative":
#                     token.created = datetime.datetime.now()
#                     token.save()
#                 else:
#                     last_token = token.key
#                     token.delete()
#                     token, created = Token.objects.get_or_create(user=user)
#
#             ser = UserSerializer(user)
#             content = ser.data
#
#             content["token"] = token.key
#             return Response(content, status=200, content_type='application/json')
#
#         else:
#             return Response(serializer.errors, status=401)