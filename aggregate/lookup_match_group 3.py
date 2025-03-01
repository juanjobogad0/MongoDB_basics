from pymongo import MongoClient
from datetime import datetime

db = MongoClient()["hacienda"]
coleccion_ldiario = db["librodiario"]

# Devuelve el monto total de la cuenta filtrado por fecha especifica o anho
filtro_por_fecha = False  # True -> Filtra por fecha específica, False -> Filtra por año
fecha_especifica = datetime(2025, 2, 28)  # Solo si filtro_por_fecha = True
año_consulta = 2023  # Solo si filtro_por_fecha = False

# Construcción dinámica del filtro
match_condition = {}

if filtro_por_fecha:
    match_condition["fecha"] = fecha_especifica
else:
    match_condition["fecha"] = {
        "$gte": datetime(año_consulta, 1, 1),
        "$lt": datetime(año_consulta + 1, 1, 1),
    }

# Pipeline con filtro dinámico
pipeline = [
    {"$match": match_condition},
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

# Ejecutar el pipeline
resultado = list(coleccion_ldiario.aggregate(pipeline))

# Mostrar resultados
for doc in resultado:
    print(f"El saldo total de la cuenta {doc['_id']} es {doc['total']}")
