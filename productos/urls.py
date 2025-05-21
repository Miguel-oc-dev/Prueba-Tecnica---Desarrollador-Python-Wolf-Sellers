from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# Router principal de la API
api_router = DefaultRouter()
api_router.register(prefix='catalogo', viewset=ProductoViewSet, basename='catalogo-productos')

urlpatterns = [
    path('api/v1', include(api_router.urls)),
]
