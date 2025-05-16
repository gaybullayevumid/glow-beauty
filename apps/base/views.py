from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = NewCategorySerializer
