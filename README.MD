# MONGODB BASICS FUNCTIONS AND OPERATORS

### CRUD Operations  
### Query operations with `aggregate()`  
### Operators: $match, $group, $lookup, $project, $sum, and $sort  

## THE DATABASE  

It simulates 100 basic accounting records for a company, consisting of two collections:

- **`librodiario`**: contains all documents with 100 random accounting records.  
- **`cuenta`**: contains the account names with their '_id', which is also found as 'cuenta_id' in the **`librodiario`** collection.  

The documents in the `librodiario` collection were generated using the Faker library. Below is the code:



```python
from faker import Faker
from pymongo import MongoClient
import random
from bson import ObjectId
from datetime import datetime

fake = Faker("es_ES")

# Possible values for cuenta_id
cuenta_ids = [
    ObjectId("67b4d3c89f468d2d5ab9e97a"),
    ObjectId("67b4d3cd9f468d2d5ab9e97b"),
    ObjectId("67b4d8a212103027586da408"),
    ObjectId("67b4d9fb7a959f6b7cca75d6"),
    ObjectId("67b4e7f9e67aaf02b31d2a43"),
    ObjectId("67b5c23943e6fd5fa99f0cdd"),
]

# Generate a single record
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

# Generate 100 records
records = [generate_record() for _ in range(100)]

# Connecting to MongoDB
cliente = MongoClient("mongodb://localhost:27017/")  # Conectar al servidor MongoDB local
db = cliente["hacienda"]  
collection = db["librodiario"]  

# Insert the generated records
collection.insert_many(records)  

print(f“{len(records)} records have been inserted into the collection 'librodiario'.”)
