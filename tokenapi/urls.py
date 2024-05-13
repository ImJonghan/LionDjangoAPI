from django.urls import path
from .views import CustomAuthToken, CreateUserView
# from tokenapi.views import CustomAuthToken

urlpatterns = [
    path("api-token-auth/", CustomAuthToken.as_view()),
]