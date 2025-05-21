from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuracion del ewsquema para la documentacion interactiva
schema_view = get_schema_view(
    openapi.Info(
        title = "API de Productos",
        default_version = 'v1',
        description="API RESTful para la gestión de productos",
        contact=openapi.Contact(email="miguel.oc.dev@gmail.com"),
    ),
    public = True,
    permission_classes=[permissions.AllowAny],
)
"""
    Rutas para: 
    1.- Panel de administración de Django
    2.- API de productos
    3.- Documentación Swaggede la API
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('productos.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
