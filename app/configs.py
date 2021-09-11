import configparser
import os

ENV = os.environ.get('ENV', 'DEV')
if ENV not in ('DEV', 'STAGING', 'PROD'):
    raise RuntimeError(
        f'Environment "{ENV}" is not recognized. Check your environment variable to make'
        'sure that the environment variable ENV is set to one of "DEV", "STAGING" or "PROD".'
    )

config = configparser.ConfigParser()
file = config.read(f"./configs/{ENV.lower()}.ini")
if not file:
    raise RuntimeError('Unable to read config file.')

db_config = config['Database']
POSTGRES_USER = db_config.get('postgres_user')
POSTGRES_PASSWORD = db_config.get('postgres_password')
POSTGRES_HOST = db_config.get('postgres_host')
POSTGRES_PORT = db_config.get('postgres_port', '5432')
POSTGRES_DB = db_config.get('postgres_db', 'elomatchmaking')
POSTGRES_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
