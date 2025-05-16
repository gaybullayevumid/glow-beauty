from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Bu email allaqachon mavjud.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])

        if user is None:
            raise serializers.ValidationError("Email yoki parol noto‘g‘ri")
        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi aktiv emas")

        data['user'] = user
        return data
