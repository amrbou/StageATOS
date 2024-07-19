from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, get_products_from_tmf,TelephonyProductViewSet, InternetProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'telephony-products', TelephonyProductViewSet, basename='telephony-product')
router.register(r'internet-products', InternetProductViewSet, basename='internet-product')

urlpatterns = [
    path('', include(router.urls)),
    path('tmf/products/', get_products_from_tmf, name='get_products_from_tmf'),
]