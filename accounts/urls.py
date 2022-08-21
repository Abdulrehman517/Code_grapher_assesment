from django.urls import path
from django.conf.urls import url

from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.Views.SignUp import SignUpView
from accounts.Views.userlist import UserAPIView

urlpatterns = [

    path("userlist/", UserAPIView.as_view(), name="user_detail"),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'signup', SignUpView.as_view()),

]