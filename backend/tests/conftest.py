from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import (
    AttributeFactory,
    AttributeValueFactory,
    CategoryFactory,
    ProductFactory,
    ProductLineFactory,
    ProductImageFactory,
    ProductTypeFactory,
    ProductLineAttributeValueFactory,
)
import pytest

register(AttributeFactory)
register(AttributeValueFactory)
register(CategoryFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)
register(ProductTypeFactory)
register(ProductLineAttributeValueFactory)

# How to access it
# category_factory


@pytest.fixture
def api_client():
    return APIClient
