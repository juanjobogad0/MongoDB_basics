from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import math
from database import base


## DEVUELVE LA CUENTA CON EL TOTAL DE LA MISMA ##
db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

nombre_cuenta = input("Ingrese el nombre de una cuenta: ")
cuenta = coleccion_cuentas.find_one({"nombre_cuenta": nombre_cuenta})

if cuenta:
    cuenta_id = cuenta["_id"]

    pipeline = [
        {"$match": {"cuenta_id": cuenta_id}},  # Filtrar por cuenta
        {"$group": {"_id": None, "total": {"$sum": "$monto"}}},  # Sumar montos
    ]

    resultado = list(coleccion_ldiario.aggregate(pipeline))

    if resultado:
        total = resultado[0]["total"]
        print(
            f"Total en {nombre_cuenta}: "
            + "{:,.2f}".format(total)
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    else:
        print(f"No existen transacciones en {nombre_cuenta}")


else:
    print("NO EXISTE ESTA CUENTA")
    print("NO EXISTE ESTA CUENTA")
    print("NO EXISTE ESTA CUENTßA")
