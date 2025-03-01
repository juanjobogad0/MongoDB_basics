from pymongo import MongoClient
from database import base
from bson import ObjectId
from datetime import datetime

## Devuelve el total de las cuentas filtrado por annho
db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

año_consulta = 2023

pipeline = [
    {
        "$match": {
            "fecha": {
                "$gte": datetime(año_consulta, 1, 1),
                "$lt": datetime(año_consulta + 1, 1, 1),
            }
        }
    },
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
