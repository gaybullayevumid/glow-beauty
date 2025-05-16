from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny

# Create your views here.

class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Foydalanuvchi muvaffaqiyatli yaratildi"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'Tizimga muvaffaqiyatli kirdingiz'})
        else:
            return Response({'error': 'Login yoki parol noto‘g‘ri'}, status=status.HTTP_401_UNAUTHORIZED)
    

class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Muvaffaqiyatli chiqildi (logout bo‘ldi)'}, status=status.HTTP_200_OK)