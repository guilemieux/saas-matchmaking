# elo-matchmaking
SaaS matchmaking system for ELO-based games

## Installation

1. Install the python dependencies: `pipenv install`
2. Install a local version of the database`docker compose up --build --remove-orphans -d`
3. Run the app locally: `uvicorn main:app --reload`
