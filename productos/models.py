from django.db import models

class Producto(models.Model):
    nombre = models.CharField("Nombre del producto", max_length=100)
    descripcion = models.TextField("Descripción del producto", blank=True, null=True)
    precio = models.DecimalField("Precio en MXN", max_digits=10, decimal_places=2)
    disponible = models.BooleanField("¿Está disponible?", default=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"