from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import CategoryFactory, BrandFactory, ProductFactory, ProductLineFactory
import pytest

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)

# How to access it
# category_factory


@pytest.fixture
def api_client():
    return APIClient
