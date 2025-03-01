from pymongo import MongoClient
from database import base

db = base()
coleccion_ldiario = db["librodiario"]
coleccion_cuentas = db["cuentas"]

## DEVUELVE TODOS LOS DOCUMENTOS EN UNA COLECCION ##
documentos = coleccion_ldiario.find()
for doc in documentos:
    print(doc)
