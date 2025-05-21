from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):

    """
        Viewset para la gestión de productos del cátalogo.
        Permite las operaciones CRUD
    """

    # Obtiene todos los productos, puede filtrarse o paginarse
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
