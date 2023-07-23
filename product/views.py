from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from product.models import Category, Brand, Product
from product.serializers import CategorySerializer, BrandSerializer, ProductSerializer


# Create your views here.
class CategoryViewSet(ViewSet):

    """
    A simple ViewSet for wiewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BrandViewSet(ViewSet):

    """
    A simple ViewSet for wiewing brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(ViewSet):

    """
    A simple ViewSet for wiewing products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
