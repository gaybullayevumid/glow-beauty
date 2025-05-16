from rest_framework import serializers
from .models import NewCategory

class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCategory
        fields = ['id', 'name', 'image']
