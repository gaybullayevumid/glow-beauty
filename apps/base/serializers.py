from rest_framework import serializers
from .models import Category

class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']
