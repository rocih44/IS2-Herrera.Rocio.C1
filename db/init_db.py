from db.database import Base, engine
from models import models_Libro, models_Usuario, models_Prestamo, models_Multa

# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente.")
