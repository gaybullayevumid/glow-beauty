from django.urls import path
from .views import SignupAPIView, LoginAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
