from pymongo import MongoClient, errors

from api import get_data_from_api
from services.logger import log_error, log_info


def get_db():
    """
    connect to local MongoDb
    :return:
    """
    client = MongoClient('localhost', 27017)
    db = client.pymongo # create database
    return client, db


def insert_data_if_empty(collection_name, api_url):
    client, db = get_db()
    collection = db[collection_name]
    if collection.count_documents({}) == 0:
        try:
            response = get_data_from_api(api_url)
            collection.insert_many(response)
            log_info(f'action: try insert sead date to {collection_name} collection')
        except errors.PyMongoError as e:
            log_error(f'action: try insert sead date to {collection_name} collection, error: {e}')
            print(f'Error: {e}')
            return e
        finally:
            client.close()