from pymongo import MongoClient
from bson import ObjectId
from database import base


db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

## ACTUALIZAR UN SOLO DOCUMENTO ##
filtro = {"_id": ObjectId("67bf78b75051d8792abf5bac")}
actualizacion = {"$set": {"detalle": "fees"}}
resultado = coleccion_ldiario.update_one(filtro, actualizacion)
print(f"Se acutalizo: {resultado.modified_count}")
