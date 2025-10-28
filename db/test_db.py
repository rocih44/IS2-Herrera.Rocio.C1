# db/test_db.py
from db.database import SessionLocal
from models.models_Usuario import Usuario
from models.models_Libro import Libro
from models.models_Prestamo import Prestamo
from models.models_Multa import Multa
from datetime import date, timedelta

# Crear sesión
db = SessionLocal()

# ----------------- USUARIOS -----------------
print("Creando usuario...")
usuario1 = Usuario(nombre="Pedro", apellido="Ruiz diaz", email="pedrod@email.com", es_socio=True)
usuario2 = Usuario(nombre="Roxana", apellido="Arriola", email="roxy@email.com", es_socio=True)

db.add(usuario1)
db.add(usuario2)
db.commit()

print("Usuarios creados correctamente:")
for u in db.query(Usuario).all():
    print(u.id, u.nombre, u.apellido, u.email, u.es_socio)

# ----------------- LIBROS -----------------
print("\nCreando libros...")
libro1 = Libro(titulo="Martin Fierro", autor="Jose Hernandez", genero="Gauchesco", estado_disponible=True, stock=3)
libro2 = Libro(titulo="Carrie", autor="Stephen King", genero="Terror", estado_disponible=True, stock=2)

db.add(libro1)
db.add(libro2)
db.commit()

print("Libros creados correctamente:")
for l in db.query(Libro).all():
    print(l.id, l.titulo, l.autor, l.genero, l.estado_disponible, l.stock)

# ----------------- PRESTAMOS -----------------
print("\nCreando préstamos...")
prestamo1 = Prestamo(
    usuario=usuario1,
    libro=libro1,
    fecha_prestamo=date.today(),
    fecha_devolucion_esperada=date.today() + timedelta(days=14)
)

prestamo2 = Prestamo(
    usuario=usuario2,
    libro=libro2,
    fecha_prestamo=date.today(),
    fecha_devolucion_esperada=date.today() + timedelta(days=7)
)

db.add(prestamo1)
db.add(prestamo2)
db.commit()

print("Préstamos creados correctamente:")
for p in db.query(Prestamo).all():
    print(p.id, p.usuario.nombre, p.libro.titulo, p.fecha_prestamo, p.fecha_devolucion_esperada)

# ----------------- MULTAS -----------------
print("\nCreando multas...")
multa1 = Multa(dias_atraso=3)
multa2 = Multa(dias_atraso=5)

db.add(multa1)
db.add(multa2)
db.commit()

print("Multas creadas correctamente:")
for m in db.query(Multa).all():
    print(m.id, m.dias_atraso)

# Cerrar sesión
db.close()
print("\n¡Test de base de datos completado!")
