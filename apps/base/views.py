from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
