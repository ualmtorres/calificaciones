# README.md

# Calificaciones Frontend

Este proyecto es una aplicación web desarrollada en Python utilizando Flask que consume una API REST para mostrar calificaciones. La interfaz de usuario está diseñada con Bootstrap para proporcionar un aspecto moderno y responsivo.

## Estructura del Proyecto

- `src/app.py`: Punto de entrada de la aplicación. Configura el servidor web y define las rutas.
- `src/templates/index.html`: Plantilla HTML que muestra las calificaciones en una tabla utilizando Bootstrap.
- `src/static/style.css`: Estilos personalizados para ajustar el diseño de la interfaz de usuario.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar la aplicación.
- `Dockerfile`: Instrucciones para construir la imagen del contenedor.
- `README.md`: Documentación del proyecto.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Asegúrate de tener Docker y Docker Compose instalados.

## Ejecución

Para ejecutar la aplicación, utiliza Docker Compose. En la terminal, ejecuta el siguiente comando:

```
docker-compose up --build
```

Esto construirá y levantará los servicios definidos en el archivo `docker-compose.yml`. La API estará disponible en `http://localhost:5000` y el frontend en `http://localhost:8000`.

## Dependencias

Las dependencias del proyecto están listadas en `requirements.txt`. Asegúrate de que estén instaladas para que la aplicación funcione correctamente.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.