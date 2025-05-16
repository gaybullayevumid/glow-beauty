from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]
