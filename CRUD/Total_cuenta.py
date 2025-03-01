from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import math
from database import base

# Devuelve el total de un cuenta especifica a traves de la varible total y con for
db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

cuenta = input("Ingrese el nombre de una cuenta: ")
cuenta = coleccion_cuentas.find_one({"nombre_cuenta": cuenta})

if cuenta:
    nombre_cuenta = cuenta["nombre_cuenta"]
    cuenta_id = cuenta["_id"]

    total = 0
    filtro = coleccion_ldiario.find({"cuenta_id": cuenta_id})
    for registros in filtro:
        montos = registros["monto"]
        total += montos

    if total == 0:
        print(f"No exiten transacciones en {nombre_cuenta}")

    else:
        print(
            "{:,.2f}".format(total)
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )


else:
    print("NO EXISTE ESTA CUENTA")
