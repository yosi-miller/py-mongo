from database.model import injuries_info, crash_document
from repository.csv_repository import read_csv
from tests.conftest import crash_db_collection

def test_insert_crash(crash_db_collection):
    csv_path = 'C:\\Users\y0504\Desktop\Week 5(10-10)\data\Traffic_Crashes_-_Crashes - 20k rows.csv'

    csv_reader = read_csv(csv_path)
    row = next(csv_reader)
    injuries_document = injuries_info(row)
    injuries_id = crash_db_collection[1].insert_one(injuries_document).inserted_id
    document = crash_document(row, injuries_id)
    crash_db_collection[0].insert_one(document)

    assert injuries_id is not None
    assert document is not None
    assert crash_db_collection[0].count_documents({}) == 1
    assert crash_db_collection[1].count_documents({'_id': injuries_id}) == 1

def indexed_test(crash_db_collection):
    pass


