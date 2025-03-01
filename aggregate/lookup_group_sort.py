from pymongo import MongoClient
from database import base
from bson import ObjectId
from datetime import datetime

## Devuelve el dia con mayor movimiento con el monto
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
        "$group": {
            "_id": "$fecha",
            "total_monto": {"$sum": "$monto"},
        },
    },
    {"$sort": {"total_monto": -1}},
]


resultado = list(coleccion_ldiario.aggregate(pipeline))
fecha_obj = resultado[0]["_id"]
fecha_str = fecha_obj.strftime("%Y-%m-%d")
print(
    f"El dia {fecha_str} tuvo el mayor movimiento de Gs {resultado[0]['total_monto']}"
)
