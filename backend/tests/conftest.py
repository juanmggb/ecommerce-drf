from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import (
    AttributeFactory,
    AttributeValueFactory,
    CategoryFactory,
    BrandFactory,
    ProductFactory,
    ProductLineFactory,
    ProductImageFactory,
    ProductTypeFactory,
)
import pytest

register(AttributeFactory)
register(AttributeValueFactory)
register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)
register(ProductTypeFactory)

# How to access it
# category_factory


@pytest.fixture
def api_client():
    return APIClient
