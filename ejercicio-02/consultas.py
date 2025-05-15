from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from generar_base import Pais  # Asegúrate que esta clase tenga los atributos correctos

# Conexión a la base SQLite
engine = create_engine('sqlite:///basepaises.db')
Session = sessionmaker(bind=engine)
session = Session()

# 1. Presentar todos los países del continente americano
print("1. Países del continente americano (NA y SA)")
paises_america = session.query(Pais).filter(or_(Pais.continente == "NA", Pais.continente == "SA")).all()
for p in paises_america:
    print(p.nombrePais)
print("--------------------------------")

# 2. Países de Asia ordenados por Dial
print("2. Países de Asia ordenados por Dial")
paises_asia = session.query(Pais).filter(Pais.continente == "AS").order_by(Pais.dial).all()
for p in paises_asia:
    print(f"{p.nombrePais} - Dial: {p.dial}")
print("--------------------------------")

# 3. Lenguajes de cada país
print("3. Lenguajes de cada país")
paises = session.query(Pais).all()
for p in paises:
    print(f"{p.nombrePais}: {p.lenguajes}")
print("--------------------------------")

# 4. Países de Europa ordenados por capital
print("4. Países de Europa ordenados por Capital")
paises_europa = session.query(Pais).filter(Pais.continente == "EU").order_by(Pais.capital).all()
for p in paises_europa:
    print(f"{p.nombrePais} - Capital: {p.capital}")
print("--------------------------------")

# 5. Países con 'uador' en nombre o 'ito' en capital
print("5. Países con 'uador' en el nombre o 'ito' en la capital")
paises_filtro = session.query(Pais).filter(
    or_(
        Pais.nombrePais.like("%uador%"),
        Pais.capital.ilike("%ito%")
    )
).all()
for p in paises_filtro:
    print(f"{p.nombrePais} - Capital: {p.capital}")
print("--------------------------------")
