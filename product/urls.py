from django.urls import path
from rest_framework.routers import DefaultRouter

from product import views

router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet, basename="categories")
router.register(r"products", views.ProductViewSet, basename="products")
urlpatterns = router.urls
