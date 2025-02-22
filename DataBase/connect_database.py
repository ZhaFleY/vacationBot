from sqlalchemy import create_engine, Text, VARCHAR, Integer, DATE, Column
from sqlalchemy.orm import sessionmaker
from env_admin import db_url
from sqlalchemy.orm import DeclarativeBase



engine  = create_engine(db_url)
Base = DeclarativeBase()

Session_local = sessionmaker(bind=engine)


class Employers(Base):
    __tablename__ = "employers"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    start_vacation = Column(DATE, nullable=False)
    end_vacation = Column(DATE, nullable=False)