from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        max_length=100,
        required=True,
        help_text="Nómbre único del producto."
    )
    descripcion = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text="Descripción inicial del producto"
    )
    precio = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        help_text="Precio en pesos mexicanos"
    )

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'disponible',
        ]
        read_only_fields = ['id']