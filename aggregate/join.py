from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import math
from database import base


## Devuelve todos los registros asociando las colecciones mediante lookup ##
db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

pipeline = [
    {
        "$lookup": {
            "from": "cuentas",
            "localField": "cuenta_id",
            "foreignField": "_id",
            "as": "cuenta_info",
        }
    },
    {"$unwind": "$cuenta_info"},  # Desanida el array para que sea un objeto único
    {
        "$project": {
            "fecha": 1,
            "_id": 0,
            "detalle": 1,
            "nombre_cuenta": "$cuenta_info.nombre_cuenta",
        }
    },
]


resultado = list(coleccion_ldiario.aggregate(pipeline))
for doc in resultado:
    print(doc)
