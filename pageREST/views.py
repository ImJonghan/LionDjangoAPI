from rest_framework import viewsets
from .models import Product
from .serializers import ProductPageSerializer
from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 1

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductPageSerializer
    pagination_class = ProductPagination
