from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from product.models import Category, Brand, Product
from product.serializers import CategorySerializer, BrandSerializer, ProductSerializer
from rest_framework.decorators import action

from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.sql import SqliteConsoleLexer, SqlLexer
from sqlparse import format
from django.db.models import Prefetch


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

    queryset = Product.objects.all().isactive()

    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug)
            .select_related("category", "brand")
            .prefetch_related(Prefetch("product_line__product_image"))
            .prefetch_related(Prefetch("product_line__attribute_value__attribute")),
            many=True,
        )
        # x = self.queryset.filter(slug=slug)
        # sqlformatter = format(str(x.query), reindent=True)
        # print(highlight(sqlformatter, SqlLexer(), TerminalFormatter()))
        # return Response(serializer.data)

        data = Response(serializer.data)

        q = list(connection.queries)
        print(len(q))
        for qs in q:
            sqlformatted = format(str(qs["sql"]), reindent=True)
            print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        return data

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)/all",
    )
    def list_product_by_category_slug(self, request, slug=None):
        """
        An endpoint to return products by category
        """
        serializer = ProductSerializer(
            self.queryset.filter(category__slug=slug), many=True
        )

        return Response(serializer.data)
