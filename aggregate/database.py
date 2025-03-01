from pymongo import MongoClient


cliente = MongoClient("mongodb://localhost:27017/")


def base():
    return cliente["hacienda"]
