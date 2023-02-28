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