from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
import requests 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

TMF_API_URL = 'http://localhost:8620/tmf-api/productCatalogManagement/v5/productCatalog'

@api_view(['GET'])
def get_products_from_tmf(request):
    try:
        response = requests.get(TMF_API_URL)
        response.raise_for_status()
        data = response.json()
        return Response(data)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['brand', 'product_type']
    
class TelephonyProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(product_type='telephony')

class InternetProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(product_type='internet')