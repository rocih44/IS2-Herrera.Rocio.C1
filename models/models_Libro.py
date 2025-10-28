from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    genero = Column(String, nullable=True)
    estado_disponible = Column(Boolean, default=True)
    stock = Column(Integer, default=1)
