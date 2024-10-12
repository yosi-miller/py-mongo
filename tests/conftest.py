import pymongo
import pytest

from database.model import crash_document, injuries_info
from repository.csv_repository import read_csv


@pytest.fixture
def init_db():
    client = pymongo.MongoClient('localhost', 27017)
    test_db = client['test_db']
    yield test_db
    client.drop_database('test_db')
    client.close()

@pytest.fixture
def crash_db_collection(init_db):
    crash_collection = init_db['crash_test']
    return crash_collection

# WARRING: from hear writer with gpt
@pytest.fixture
def populate_crash_db(crash_db_collection):
    for row in read_csv('C:\\Users\y0504\Desktop\Week 5(10-10)\data\‏test_data.csv'):
        injuries = injuries_info(row)
        document = crash_document(row, injuries)
        crash_db_collection.insert_one(document)