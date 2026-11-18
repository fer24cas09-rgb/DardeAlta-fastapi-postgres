# API de estudiantes, maestros y personal (FastAPI + PostgreSQL)

API REST hecha con FastAPI que se conecta a una base de datos PostgreSQL
y consulta estudiantes, maestros y personal.

## Tecnologías
- Python
- FastAPI y Uvicorn
- PostgreSQL con psycopg
- python-dotenv

## Endpoints
- GET /db-test: prueba la conexión con la base de datos
- GET /estudiantes: lista de estudiantes
- GET /maestros: lista de maestros
- GET /personal: lista de personal

## Cómo ejecutarlo
1. Clona el repositorio
2. Crea y activa un entorno virtual
3. Instala las dependencias: pip install -r requirements.txt
4. Copia .env.example como .env y llena tus datos de PostgreSQL
5. Ejecuta: uvicorn main:app --reload
6. Abre http://127.0.0.1:8000/docs para ver la documentación

## Autor
Fernando Castillo Sandoval
