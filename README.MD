# MONGODB BASICS FUNCTIONS AND OPERATORS

### CRUD Operations  
### Query operations with `aggregate()`  
### Operators: $match, $group, $lookup, $project, $sum, and $sort  

## THE DATABASE  

It simulates 100 basic accounting records for a company, consisting of two collections:

- **`librodiario`**: contains all documents with 100 random accounting records.  
- **`cuenta`**: contains the account names with their '_id', which is also found as 'cuenta_id' in the **`librodiario`** collection.  

The documents in the `librodiario` collection were generated using the Faker library:



