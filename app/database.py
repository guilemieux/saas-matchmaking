import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext import declarative

import configs

engine = sa.create_engine(configs.POSTGRES_URL)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()
