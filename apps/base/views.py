from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class NewCategoryListCreateView(generics.ListCreateAPIView):
    queryset = NewCategory.objects.all()
    serializer_class = NewCategorySerializer
