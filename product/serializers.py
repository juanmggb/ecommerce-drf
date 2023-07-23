from rest_framework import serializers
from product.models import Category, Brand, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"

        fields = ("name",)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
