from decouple import config

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine(
    config("MY_DATABASE"),
    echo=True,
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
