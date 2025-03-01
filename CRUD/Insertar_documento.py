from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from database import base

db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

## INSERTAR UN DOCUMENTO NUEVO EN LA COLECCION LIBRODIARIO MEDIANTE INSERT_ONE

# Buscar la cuenta por nombre
nombre_cuenta = "provistas"
cuenta = coleccion_cuentas.find_one({"nombre_cuenta": nombre_cuenta})

if cuenta:
    cuenta_id = cuenta["_id"]

    nuevo_asiento = {
        "fecha": datetime(2020, 12, 12),
        "detalle": "carne, perro, mano",
        "monto": 134341345,
        "fact": "fact-16",
        "cuenta_id": cuenta_id,
    }

    resultado = coleccion_ldiario.insert_one(nuevo_asiento)
    print(f"Se agregó nuevo asiento con ID: {resultado.inserted_id}")

else:
    print(f"No se encontró la cuenta '{nombre_cuenta}' en la base de datos.")
    print(f"No se encontró la cuenta '{nombre_cuenta}' en la base de datos.")
    print(f"No se encontró la cuenta '{nombre_cuenta}' en la base de datos.")
