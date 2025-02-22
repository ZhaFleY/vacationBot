from DataBase.connect_database import Session_local,Base
from sqlalchemy import create_engine, Text, VARCHAR, Integer, DATE, Column

session = Session_local()
Base=Base


class Employers_Vacations(Base):
    __tablename__ = "employers"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    start_vacation = Column(DATE, nullable=False)
    end_vacation = Column(DATE, nullable=False)


class Employers(Base):
    __tablename__= "employersauth"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    last_name=Column(VARCHAR(200), nullable=False)
    telegram_id=Column(VARCHAR(200), nullable=False)