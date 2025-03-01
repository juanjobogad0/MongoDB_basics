from pymongo import MongoClient
from bson import ObjectId
from database import base

db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

## INSERTA VARIOS DOCUEMNTOS EN UNA COLECCION
nuevos_nombre = [
    {"nombre_cuenta": "carlos"},
    {"nombre_cuenta": "jose"},
    {"nombre_cuenta": "pepe"},
    {"nombre_cuenta": "carlos"},
    {"nombre_cuenta": "raul"},
]


resultado = coleccion_cuentas.insert_many(nuevos_nombre)
print(f" Se han insertado {resultado.inserted_ids}")
