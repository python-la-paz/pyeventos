# ¡Bienvenidos al repositorio de Eventos de Python La Paz *_Python La Paz_* ! 💻🚀

En este repositorio encontrarás un administrador de eventos libre con el cual podrás construir y armar la página de presentación de tu evento de manera sencilla,

Apoyado por la comunidad, desarrollado por la comunidad, para la comunidad.

## Aquí encontrarás 📋 una demo

[Demo Evento](https://pyday.pylapaz.org/demo/)

## Características 📌

- **Eventos**: Crea eventos y comparte la información de tu evento.
- **Segmentos**: Crea segmentos y comparte la información de tu segmento en un orden específico.
  - Añade detalles de segmentos, con 3 formatos con imagen a la izquierda, derecha o sin imagen.
  - Añade la ubicación de tu evento con Google Maps.
  - Añade patrocinadores de tu evento.
  - Añade videos de tu evento.
  - Añade cronograma de tu evento, por sala y por día.
  - Añade los precios de tu evento como un tier list.
  - Añade un espacio para Sponsors y Colaboradores.

## Clona el repositorio 📦

Puedes acceder al proyecto clonando el repositorio y ejecutando el siguiente comando.

```bash
python manage.py runserver
```

## Despliegue  🚀

Solo necesitas tener instalado Docker y Docker Compose en tu máquina, y ejecutar alguno de los siguientes comandos.

# Deploy compose on local build images
```sh
cp backend.env backend/.env
cp database.env database/.env
docker-compose -f .\docker-compose.dev.yaml up -d --build
docker-compose -f .\docker-compose.dev.yaml exec -it app python manage.py createsuperuser
```
# Deploy compose on local prod using image in Docker Hub
```sh
cp backend.env backend/.env
cp database.env database/.env
docker-compose -f .\docker-compose.prod.local.yaml up -d --build
docker-compose -f .\docker-compose.prod.local.yaml exec -it app python manage.py createsuperuser
```

# Deploy with traefik using image in Docker Hub
```sh
cp backend.env backend/.env
cp database.env database/.env
cp traefik.env .env
docker-compose -f .\docker-compose.prod.traefik.arm64.yaml -d --build
docker-compose -f .\docker-compose.prod.traefik.arm64.yaml exec -it app python manage.py createsuperuser
```

  
### Con mucho ❤️ Python La Paz 🐍 
[![Pagina Web](https://img.shields.io/badge/Web-Python%20La%20Paz-blue.svg)](https://pylapaz.org/)

