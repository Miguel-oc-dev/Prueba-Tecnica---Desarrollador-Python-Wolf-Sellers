from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from productos.models import Producto

class ProductoAPITestCase(APITestCase):
    """
        Pruebas para verificar el comportamiento de la API de productos.
        Cubre operaciones CRUD
    """

    def setUp(self):
        # Producto inicial para pruebas de lectura, actualización y eliminación
        self.producto = Producto.objects.create(
            nombre="Producto de prueba",
            descripcion="Descripción de prueba",
            precio="9.99",
            disponible=True
        )
        self.list_url = reverse('producto-list')
        self.detail_url = lambda pk: reverse('producto-detail', kwargs={'pk': pk})


    def test_listar_productos(self):
        """Verifica que la API devuelve la lista de productos correctamente"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "La respuesta debe ser 200 OK al listar productos")


    def test_crear_producto(self):
        """Verifica que se puede crear un producto correctamente mediante POST"""
        data = {
            "nombre": "Nuevo Producto",
            "descripcion": "Un producto creado en test",
            "precio": "19.99",
            "disponible": True
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Debe retornar 201 al crear un producto")
        self.assertEqual(Producto.objects.count(), 2, "Debe haber 2 productos en total tras la creación")


    def test_obtener_producto(self):
        """Verifica que se puede obtener un producto existente por ID"""
        response = self.client.get(self.detail_url(self.producto.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.producto.nombre)


    def test_actualizar_producto(self):
        """Verifica que se puede actualizar un producto existente mediante PUT"""
        data = {
            "nombre": "Producto Actualizado",
            "descripcion": "Actualizado desde test",
            "precio": "29.99",
            "disponible": False
        }
        response = self.client.put(self.detail_url(self.producto.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.nombre, "Producto Actualizado")


    def test_eliminar_producto(self):
        """Verifica que se puede eliminar un producto correctamente"""
        response = self.client.delete(self.detail_url(self.producto.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Producto.objects.count(), 0)


    def test_creacion_invalida(self):
        """Verifica que no se puede crear un producto sin nombre (campo requerido)"""
        data = {
            "descripcion": "Sin nombre",
            "precio": "10.00",
            "disponible": True
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("nombre", response.data)
