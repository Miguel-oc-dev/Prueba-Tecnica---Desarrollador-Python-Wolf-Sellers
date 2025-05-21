
# 🐺 Prueba Técnica - Microservicio de Productos con Django REST Framework

Este microservicio gestiona productos utilizando Django 4.2+ y Django REST Framework, implementado con SQLite y ejecutable vía Docker.

---

## 🚀 Requisitos

- Python 3.10+
- Docker y Docker Compose
- Git (para clonar el repositorio)

---

## ⚙️ Instalación local (sin Docker)

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/nombre-repositorio.git
cd nombre-repositorio
```

2. Crea y activa un entorno virtual:

```bash
python -m venv env
En Windows: env\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta migraciones:

```bash
python manage.py migrate
```

5. Ejecuta el servidor:

```bash
python manage.py runserver
```

---

## 🐳 Instalación con Docker

1. Asegúrate de tener Docker y Docker Compose instalados.
2. Construye y ejecuta los contenedores:

```bash
docker compose up --build
```

3. El servicio estará disponible en:

```
http://localhost:8000
```

![image](https://github.com/user-attachments/assets/5b7a9808-233a-4250-9597-68dfc7e5255c)


---

## 📦 Endpoints de la API

| Método | Endpoint              | Descripción              |
|--------|-----------------------|--------------------------|
| GET    | /api/productos/       | Lista todos los productos |
| POST   | /api/productos/       | Crea un nuevo producto   |
| GET    | /api/productos/{id}/  | Consulta un producto por ID |
| PUT    | /api/productos/{id}/  | Actualiza un producto    |
| DELETE | /api/productos/{id}/  | Elimina un producto      |

![image](https://github.com/user-attachments/assets/f1e3a41f-9905-4c3f-b080-5cedf9732660)

![image](https://github.com/user-attachments/assets/9d3b16da-37a2-431c-bfff-3e29116e639e)


---

## 🔎 Ejemplo de JSON para crear producto

```json
{
  "nombre": "Auriculares Bluetooth",
  "descripcion": "Auriculares inalámbricos con cancelación de ruido",
  "precio": "1499.99",
  "disponible": true
}
```

---

## 🧪 Correr pruebas

Puedes ejecutar las pruebas unitarias con el siguiente comando:

```bash
python manage.py test
```

Si estás en Docker:

```bash
docker compose exec web python manage.py test
```

---

## 🧭 Swagger

La documentación se puede consultar si se instala `drf-yasg`:

```bash
pip install drf-yasg
```

Y agregas en tu `urls.py`:

```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API de Productos",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # ...
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```

---

## 📄 Desarrollado por Miguel Contreras
