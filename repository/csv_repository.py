import csv
from pymongo import errors
from database.connect import get_db
from database.model import crash_document, injuries_info
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

    crash_collection = db['crash information']
    injuries_collection = db['injuries information']

    if crash_collection.count_documents({}) == 0:
        try:
            for row in read_csv('data/Traffic_Crashes_-_Crashes - 20k rows.csv'):
                injuries_document = injuries_info(row)

                injuries_id = injuries_collection.insert_one(injuries_document).inserted_id

                document = crash_document(row, injuries_id)

                crash_collection.insert_one(document)

            log_info(f'action: completed insert crashs information to db')

            create_index(crash_collection, injuries_collection)

        except errors.PyMongoError as e:
            log_error(f'action: try insert crashs information, error: {e}')
            print(f'Error: {e}')
            return e
        finally:
            client.close()


def create_index(crash_collection, injuries_collection):
    # create a new index for the crash document and injustice document
    crash_collection.create_index('crash_cause')
    crash_collection.create_index('beat')
    crash_collection.create_index('date')
    injuries_collection.create_index('total')
    injuries_collection.create_index('injuries_status')
    log_info(f'action: completed create indexes for crashs and injuries collections')