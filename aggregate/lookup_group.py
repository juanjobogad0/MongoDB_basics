from pymongo import MongoClient
from database import base
from bson import ObjectId

# Devuelve el total de todas las cuentas
db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

pipeline = [
    {
        "$lookup": {
            "from": "cuentas",
            "localField": "cuenta_id",
            "foreignField": "_id",
            "as": "nombre",
        }
    },
    {"$unwind": "$nombre"},
    {"$group": {"_id": "$nombre.nombre_cuenta", "total": {"$sum": "$monto"}}},
]

resultado = list(coleccion_ldiario.aggregate(pipeline))
for doc in resultado:
    print(f"El saldo total de la cuenta {doc['_id']} es {doc['total']}")
