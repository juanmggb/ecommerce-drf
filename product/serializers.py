from rest_framework import serializers
from product.models import Category, Brand, Product, ProductLine, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        # fields = "__all__"

        fields = ("category_name",)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        # fields = "__all__"
        exclude = ("id",)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("id", "productline")


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = ("price", "sku", "stock_qty", "order", "product_image")
        # exclude = ("id", "product", "is_active")


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name")

    brand_name = serializers.CharField(source="brand.name")

    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        # fields = "__all__"
        # exclude = ("id",)
        fields = (
            "name",
            "slug",
            "description",
            "category_name",
            "brand_name",
            "product_line",
        )
