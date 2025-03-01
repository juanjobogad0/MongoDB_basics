from pymongo import MongoClient
from bson import ObjectId
from database import base

db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]


## ELIMINIAR UN DOCUMENTO
filtro = {"_id": ObjectId("67bf78b75051d8792abf5ba7")}
resultado = coleccion_ldiario.delete_one(filtro)
print(f"Dcoumento eliminado: {resultado.deleted_count}")
