from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.database import Base

class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    libro_id = Column(Integer, ForeignKey("libros.id"))
    fecha_prestamo = Column(Date)
    fecha_devolucion_esperada = Column(Date)
    fecha_devolucion_real = Column(Date, nullable=True)

    usuario = relationship("Usuario")
    libro = relationship("Libro")
