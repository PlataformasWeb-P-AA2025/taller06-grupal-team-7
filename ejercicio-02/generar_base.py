from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# se genera en enlace al gestor de base de
# datos
engine = create_engine('sqlite:///basepaises.db')

# Se crea la clase base para definir los modelos (entidades)
Base = declarative_base()

# Recorre cada diccionario (país) dentro de los datos obtenidos
class Pais(Base):
    __tablename__ = 'paises'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombrePais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geonameId = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    isIndependiente = Column(String)


Base.metadata.create_all(engine)

