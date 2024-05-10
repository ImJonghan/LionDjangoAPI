from django.urls import path
from .views import product_list, product_detail


urlpatterns = [
    path('products/', product_list, name='product_list'), # alt+shift+위아래 화살표    
    path('products/<int:pk>/', product_detail, name='product_detail'), # alt+shift+위아래 화살표    
]