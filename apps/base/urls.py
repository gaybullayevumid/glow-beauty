from django.urls import path, include
from .views import *

urlpatterns = [
    path('new-categories/', NewCategoryListCreateView.as_view(), name='new-category-list-create'),
    # path('products/', ProductView.as_view(), name='products'),
]
