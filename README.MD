# EJERCICIOS PARA PRACTICAR FUNCIONES Y OPERADORES DE MONGODB

### Operaciones CRUD
### Operaciones de consulta con `aggregate()`
### Operdaores $match, $group, $lookup, $project, $sum y $sort

## LA BASE DE DATOS

Simula 100 registros contables básicos de una empresa, conformada por dos colecciones:

- **`librodiario`**: donde se encuentran todos los documentos con 100 registros contables random.
- **`cuenta`**: donde se encuentran los nombres de las cuentas con su '_id', el cual tambien se encuentra como 'cuenta_id' en la coleccion **`librodiario`** .
 
Los documentos en la colección `librodiario` fueron generados con la biblioteca Faker. Comparto el código a continuación:

```python
from faker import Faker
from pymongo import MongoClient
import random
from bson import ObjectId
from datetime import datetime

fake = Faker("es_ES")

# Posibles valores para cuenta_id
cuenta_ids = [
    ObjectId("67b4d3c89f468d2d5ab9e97a"),
    ObjectId("67b4d3cd9f468d2d5ab9e97b"),
    ObjectId("67b4d8a212103027586da408"),
    ObjectId("67b4d9fb7a959f6b7cca75d6"),
    ObjectId("67b4e7f9e67aaf02b31d2a43"),
    ObjectId("67b5c23943e6fd5fa99f0cdd"),
]

# Función para generar un solo registro
def generate_record():
    fecha_str = fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d")
    fecha_iso = datetime.strptime(fecha_str, "%Y-%m-%d")  # Convertir a datetime
    
    return {
        "fecha": fecha_iso,
        "detalle": f"{fake.word()} {fake.word()}",  # Genera un detalle aleatorio (sustantivo + adjetivo)
        "monto": random.randint(100000, 100000000),
        "fact": "001" + str(random.randint(1000000, 9999999)),
        "cuenta_id": random.choice(cuenta_ids),  # Selecciona aleatoriamente un cuenta_id
    }

# Generar 100 registros
records = [generate_record() for _ in range(100)]

# Conectar a MongoDB (suponiendo que tienes MongoDB corriendo localmente)
cliente = MongoClient("mongodb://localhost:27017/")  # Conectar al servidor MongoDB local
db = cliente["hacienda"]  # Conectar a la base de datos "hacienda"
collection = db["librodiario"]  # Conectar a la colección "librodiario"

# Insertar los registros generados
collection.insert_many(records)  # Insertar los registros en la colección

print(f"{len(records)} registros han sido insertados en la colección 'librodiario'.")
