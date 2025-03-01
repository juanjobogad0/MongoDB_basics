from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from database import base

## Listar todas las transacciones de una cuenta con find_one()##
db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]


nombre_cuenta = input("Ingrese un cuenta: ")
cuenta = coleccion_cuentas.find_one({"nombre_cuenta": nombre_cuenta})

if cuenta:
    id_cuenta = cuenta["_id"]

    transacciones = coleccion_ldiario.find({"cuenta_id": (id_cuenta)}).sort("fecha", -1)

    for transaccion in transacciones:
        print(
            f"Fecha: {transaccion['fecha']}, Detalle: {transaccion['detalle']}, Monto: {transaccion['monto']}, Factura: {transaccion['fact']}"
        )


else:
    print("La cuenta no exite")
