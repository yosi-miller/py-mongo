import csv
from pymongo import errors
from database.connect import get_db
from database.model import crash_document
from services.logger import log_error, log_info


def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


def init_crash_information_from_csv():
    """
    Initializes crash information from CSV file to MongoDB collection.
    """
    client, db = get_db()

    collection = db['crash information']

    if collection.count_documents({}) == 0:
        try:
            for row in read_csv('data/Traffic_Crashes_-_Crashes - 20k rows.csv'):
                document = crash_document(row)
                collection.insert_one(document)

            log_info(f'action: completed insert crashs information to db')
        except errors.PyMongoError as e:
            log_error(f'action: try insert crashs information, error: {e}')
            print(f'Error: {e}')
            return e
        finally:
            client.close()