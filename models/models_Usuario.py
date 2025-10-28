from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    es_socio = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Usuario(nombre={self.nombre}, email={self.email})>"