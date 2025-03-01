from pymongo import MongoClient
from bson import ObjectId
from database import base

db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

## DEVUELVE UN DOCUMENTO BUSCANDO SU ID ##
filtro = coleccion_ldiario.find_one({"_id": ObjectId("67bf78b75051d8792abf5ba9")})

if filtro:
    print(filtro)
else:
    print("NO EXISTE EL DOCUMENTO")
    print("NO EXISTE EL DOCUMENTO")
    print("NO EXISTE EL DOCUMENTO")
    print("NO EXISTE EL DOCUMENTO")
