from pymongo import errors

from database.connect import get_db
from repository.api import get_data_from_api
from services.logger import log_error, log_info


def insert_data_if_empty(collection_name, api_url):
    # TODO: לחלק ל2 פונקציות
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