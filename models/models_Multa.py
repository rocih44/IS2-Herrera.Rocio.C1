from sqlalchemy import Column, Integer
from db.database import Base

class Multa(Base):
    __tablename__ = "multas"

    id = Column(Integer, primary_key=True, index=True)
    dias_atraso = Column(Integer)
