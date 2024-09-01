# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter ()
["DefaultRouter()"]
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
  ]
