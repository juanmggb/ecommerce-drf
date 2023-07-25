import factory
from product.models import (
    Category,
    Brand,
    Product,
    ProductLine,
    ProductImage,
    ProductType,
    ProductTypeAttribute,
    Attribute,
    AttributeValue,
)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # name = "test_category"
    name = factory.Sequence(lambda n: f"Category_{n}")

    # parent =


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    # name = "test_brand"
    name = factory.Sequence(lambda n: f"Brand_{n}")


class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attribute

    name = "attribute_name_test"
    description = "attr_description_test"


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = "test_type"

    @factory.post_generation
    def attribute(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        # Make sure extracted is a list of Attribute instances
        if not all(isinstance(attr, Attribute) for attr in extracted):
            raise ValueError("All 'attribute' values must be instances of Attribute.")

        # Add the extracted Attribute instances to the attribute ManyToMany field
        for attr in extracted:
            self.attribute.add(attr)


# class ProductTypeAttribute(factory.django.DjangoModelFactory):
#     class Meta:
#         model = ProductTypeAttribute

#     product_type = factory.SubFactory(ProductTypeFactory)
#     attribute = factory.SubFactory(AttributeFactory)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Product_{n}")

    description = "test_description"

    is_digital = True

    brand = factory.SubFactory(BrandFactory)

    category = factory.SubFactory(CategoryFactory)

    is_active = True

    product_type = factory.SubFactory(ProductTypeFactory)


class AttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AttributeValue

    attribute_value = "attr_test"
    attribute = factory.SubFactory(AttributeFactory)


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = 10.00
    sku = "12345"
    stock_qty = 1
    product = factory.SubFactory(ProductFactory)
    is_active = True

    @factory.post_generation
    def attribute_value(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        # Make sure extracted is a list of AttributeValue instances
        if not all(isinstance(attr_value, AttributeValue) for attr_value in extracted):
            raise ValueError(
                "All 'attribute_value' values must be instances of AttributeValue."
            )

        for attr_value in extracted:
            self.attribute_value.add(attr_value)


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    alternative_text = "test_alternative_text"
    url = "test.jpg"
    productline = factory.SubFactory(ProductLineFactory)
