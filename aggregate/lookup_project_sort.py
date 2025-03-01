from pymongo import MongoClient
from database import base
from bson import ObjectId
from datetime import datetime

## Devuelve los documentos ordenados por el monto en forma descendente ##
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
    {
        "$project": {
            "fecha": 1,
            "_id": 0,
            "monto": 1,
            "nombre_cuenta": "$nombre.nombre_cuenta",
        }
    },
    {"$sort": {"monto": -1}},
]

resultado = list(coleccion_ldiario.aggregate(pipeline))
for doc in resultado:
    fecha_obj = doc["fecha"]
    fecha_str = fecha_obj.strftime("%Y-%m-%d")
    print(
        f"El {fecha_str}, la cuenta {doc['nombre_cuenta']} con monto de: {doc['monto']}"
    )
