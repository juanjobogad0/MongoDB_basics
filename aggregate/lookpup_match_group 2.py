from pymongo import MongoClient
from database import base
from bson import ObjectId
from datetime import datetime

## Devuelve el total de las cuentas filtrado por fecha especifica
db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]


fecha_consulta = datetime(2025, 2, 28)


pipeline = [
    {
        "$lookup": {
            "from": "cuentas",  # Colección de cuentas
            "localField": "cuenta_id",  # Campo en librodiario
            "foreignField": "_id",  # Campo en cuentas
            "as": "nombre",
        }
    },
    {"$unwind": "$nombre"},
    {"$match": {"fecha": fecha_consulta}},
    {"$group": {"_id": "$nombre.nombre_cuenta", "total": {"$sum": "$monto"}}},
]

resultado = list(coleccion_ldiario.aggregate(pipeline))
for doc in resultado:
    print(f"El saldo total de la cuenta {doc['_id']} es {doc['total']}")
