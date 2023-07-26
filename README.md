# Proyecto API DE MASCOTAS DIVELIA 

API DE MASCOTAS DIVELIA 

## Descripción
Bienvenido al proyecto APIde Mascotas. Este es un proyecto desarrollado en Django que proporciona una API REST para gestionar información de desarrolladores, mascotas y juguetes asociados a las mascotas.

## Requisitos
- Python 3.10
- Django 4.2.3
- Django Rest Framework

## Instalación
1. Clona el repositorio o descarga el código fuente.
2. Crea y activa un entorno virtual (opcional pero recomendado).
3. Instala las dependencias usando pip:

```bash
pip install -r requirements.txt
```

## Uso
Accede a la API a través de la URL: http://localhost:8000/mascotas/v1/
Puedes utilizar herramientas como curl, httpie, o un cliente API como Postman para interactuar con la API.
## Endpoints
## Developers
GET /api/developers/: Obtener una lista de todos los desarrolladores.

POST /api/developers/: Crear un nuevo desarrollador.

GET /api/developers/<int:pk>/: Obtener detalles de un desarrollador por su ID.

PUT /api/developers/<int:pk>/: Actualizar los detalles de un desarrollador por su ID.

DELETE /api/developers/<int:pk>/: Eliminar un desarrollador por su ID.

## Mascotas
GET /api/mascotas/: Obtener una lista de todas las mascotas.

POST /api/mascotas/: Crear una nueva mascota.

GET /api/mascotas/<int:pk>/: Obtener detalles de una mascota por su ID.

PUT /api/mascotas/<int:pk>/: Actualizar los detalles de una mascota por su ID.

DELETE /api/mascotas/<int:pk>/: Eliminar una mascota por su ID.

## Juguetes
GET /api/juguetes/: Obtener una lista de todos los juguetes.

POST /api/juguetes/: Crear un nuevo juguete.

GET /api/juguetes/<int:pk>/: Obtener detalles de un juguete por su ID.

PUT /api/juguetes/<int:pk>/: Actualizar los detalles de un juguete por su ID.

DELETE /api/juguetes/<int:pk>/: Eliminar un juguete por su ID.

## Asociar Juguetes a Mascotas
POST /api/mascotas/<int:mascota_id>/asociar-juguete/: Asociar un juguete a una mascota por el ID de la mascota.
