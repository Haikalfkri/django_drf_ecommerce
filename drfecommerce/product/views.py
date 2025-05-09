from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

# Create your views here.
class CategoryView(viewsets.ViewSet):
    """
    A simple Viewset to viewing all categories
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class BrandView(viewsets.ViewSet):
    """
    A simple Viewset to viewing all brands
    """
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    

class ProductView(viewsets.ViewSet):
    """
    A simple Viewset to viewing all brands
    """
    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)