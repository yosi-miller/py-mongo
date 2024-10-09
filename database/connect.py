from pymongo import MongoClient

def get_db():
    """
    connect to local MongoDb
    :return:
    """
    client = MongoClient('localhost', 27017)
    db = client.pymongo # create database
    return client, db