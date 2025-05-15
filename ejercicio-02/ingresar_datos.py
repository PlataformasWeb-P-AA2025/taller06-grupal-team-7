from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
import json
from generar_base import Pais

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

# Realiza una solicitud HTTP GET a la URL y
# Convierte el contenido de la respuesta en formato JSON (lista de diccionarios)
response = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
data = response.json()

# Recorre cada diccionario (país) dentro de los datos descargados
for d in data:
    # Crea un nuevo objeto Pais con los valores correspondientes del JSON
    pais = Pais(
        nombrePais=d["CLDR display name"],
        capital=d["Capital"],
        continente=d["Continent"],
        dial=d["Dial"],
        geonameId=d["Geoname ID"],
        itu=d["ITU"],
        lenguajes=d["Languages"],
        isIndependiente=d["is_independent"]
    )
    # Agrega el objeto a la sesión
    session.add(pais)

# Confirma y guarda todos los cambios en la base de datos
session.commit()
