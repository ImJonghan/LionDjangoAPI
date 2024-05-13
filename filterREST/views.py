# views.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductFilterSerializer
from .filters import ProductFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductFilterSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter) # 사용할 필터 백엔드를 정의
    filterset_class = ProductFilter # 사용자 정의 필터 클래스 지정
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']

    # 짬뽕 WkaQhd W->ㅉ k ->ㅏ.....


# http 표준 - > 문자열

# data = {
#     'name':"짬뽕",
#     'price':15000
# }
# -> "{'name':'짬뽕','price':15000}"