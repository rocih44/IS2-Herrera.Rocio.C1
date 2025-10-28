from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --------------------------------------------------------
# 1. Crear motor de base de datos
# --------------------------------------------------------
# Usaremos SQLite para principiantes, la base de datos será un archivo
DATABASE_URL = "sqlite:///biblioteca.db"  # El archivo se creará en la carpeta principal

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesario para SQLite
)

# --------------------------------------------------------
# 2. Crear sesión de conexión
# --------------------------------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --------------------------------------------------------
# 3. Clase base para los modelos
# --------------------------------------------------------
Base = declarative_base()

# Función helper para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
