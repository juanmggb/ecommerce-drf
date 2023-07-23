import factory
from product.models import Category, Brand, Product


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


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Product_{n}")

    description = "test_description"

    is_digital = True

    brand = factory.SubFactory(BrandFactory)

    category = factory.SubFactory(CategoryFactory)
