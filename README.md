# client-service

# Client Service API

Cette API REST Django permet la gestion des comptes clients, incluant la création, la mise à jour et la suppression des comptes particuliers et entreprises.

## Fonctionnalités

- Création, mise à jour, consultation et suppression de comptes clients
- Support des clients particuliers et entreprises
- API RESTful pour les opérations clients
- Documentation Swagger intégrée

## Endpoints API

- **POST /api/clients/**: Création d'un nouveau client
- **GET /api/clients/{id}/**: Consultation d'un client par ID
- **PUT /api/clients/{id}/**: Mise à jour d'un client par ID
- **DELETE /api/clients/{id}/**: Suppression d'un client par ID

## Structure du Projet

```
client-service/
├── src/
│   ├── manage.py
│   ├── requirements.txt
│   ├── clientapi/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── clients/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Installation

1. Cloner le dépôt
```bash
git clone https://github.com/yasminealt/client-service.git
cd client-service
```

2. Créer et activer l'environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Lancer le serveur
```bash
cd src
python manage.py migrate
python manage.py runserver
```

## Documentation API

- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/
- OpenAPI JSON: http://localhost:8000/swagger.json

## Licence

Ce projet est sous licence MIT.
