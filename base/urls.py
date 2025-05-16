from django.urls import path, include
from .views import ProductView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
]
