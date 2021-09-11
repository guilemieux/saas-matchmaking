# SaaS Matchmaking

SaaS matchmaking system

## Installation

1. Install the python dependencies: `pipenv install`
2. Install a local version of the database: `docker compose up --build --remove-orphans -d`
3. Run database migration to have the latest schemas: `alembic upgrade head`
4. Run the app locally: `uvicorn app.main:app --reload`
