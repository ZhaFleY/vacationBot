from sqlalchemy import create_engine, Text, VARCHAR, Integer, DATE, Column
from sqlalchemy.orm import sessionmaker
from env_admin import db_url
from sqlalchemy.ext.declarative import declarative_base



engine  = create_engine(db_url)
Base = declarative_base()

Session_local = sessionmaker(bind=engine)


