import pymongo
import pytest
from datetime import datetime, timedelta

from database.model import crash_document


@pytest.fixture
def init_db():
    client = pymongo.MongoClient('localhost', 27017)
    test_db = client['test_db']
    yield test_db
    # client.drop_database('test_db')
    client.close()

@pytest.fixture
def crash_db_collection(init_db):
    crash_collection = init_db['crash_test']
    return crash_collection

# WARRING: from hear writer with gpt
@pytest.fixture
def populate_crash_db(crash_db_collection):
    test_data = [
        {
            'date': '10/01/2024 12:00',
            'beat': 'A1',
            'day_of_week': '5',
            'month': '10',
            'crash_cause': {'prim': 'Speeding', 'sec': 'Distraction'},
            'injuries_info': {'total': 3, 'fatal': 1, 'incapacitating': 1, 'non_incapacitating': 1}
        },
        {
            'date': '10/02/2024 14:20',
            'beat': 'A1',
            'day_of_week': '6',
            'month': '10',
            'crash_cause': {'prim': 'Distraction', 'sec': 'Speeding'},
            'injuries_info': {'total': 2, 'fatal': 0, 'incapacitating': 1, 'non_incapacitating': 1}
        },
        {
            'date': '09/28/2024 11:30',
            'beat': 'A1',
            'day_of_week': '3',
            'month': '9',
            'crash_cause': {'prim': 'Speeding', 'sec': 'Alcohol'},
            'injuries_info': {'total': 4, 'fatal': 0, 'incapacitating': 2, 'non_incapacitating': 2}
        }
    ]

    for data in test_data:
        crash_db_collection.insert_one(crash_document(data))
