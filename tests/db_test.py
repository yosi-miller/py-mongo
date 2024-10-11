from datetime import datetime

from database.model import injuries_info, crash_document
from repository.csv_repository import read_csv
from repository.query_repository import fetch_crash_data_by_period, aggregate_crashes_by_cause
from tests.conftest import crash_db_collection, populate_crash_db


def test_insert_crash(crash_db_collection):
    csv_path = 'C:\\Users\y0504\Desktop\Week 5(10-10)\data\Traffic_Crashes_-_Crashes - 20k rows.csv'

    csv_reader = read_csv(csv_path)
    row = next(csv_reader)

    injuries_document = injuries_info(row)
    document = crash_document(row, injuries_document)
    crash_db_collection.insert_one(document)

    assert document is not None
    assert crash_db_collection.count_documents({}) == 1

def test_print_db_content(crash_db_collection, populate_crash_db):
    all_crashes = list(crash_db_collection.find({}))
    print(f"All crashes in DB: {all_crashes}")
    assert len(all_crashes) == 3

def test_find_crash_by_area(crash_db_collection):
    pass


# WARRING: from hear writer with gpt
def test_fetch_crash_data_by_period(crash_db_collection, populate_crash_db):
    # Ensure the fixture runs
    populate_crash_db

    # Test for a day range
    result = fetch_crash_data_by_period("A1", "10-01-2024", "day", crash_db_collection)
    print(f"Result for day range: {result}")  # הוספת הדפסה לצורך ניפוי שגיאות
    assert result["total_crashes"] == 1
    assert result["start_date"] == datetime(2024, 10, 1)
    assert result["end_date"] == datetime(2024, 10, 2)

    # Test for a week range
    result = fetch_crash_data_by_period("A1", "09-28-2024", "week", crash_db_collection)
    print(f"Result for week range: {result}")  # הוספת הדפסה לצורך ניפוי שגיאות
    assert result["total_crashes"] == 3
    assert result["start_date"] == datetime(2024, 9, 28)
    assert result["end_date"] == datetime(2024, 10, 5)

    # בדיקת תוכן מסד הנתונים
    all_crashes = list(crash_db_collection.find({}))
    print(f"All crashes in DB: {all_crashes}")  # הוספת הדפסה לצורך ניפוי שגיאות


def test_aggregate_crashes_by_cause(crash_db_collection, populate_crash_db):
    result = aggregate_crashes_by_cause("A1", crash_db_collection)

    # נבדוק שיש אגרגציה לפי סיבת התאונה
    assert len(result) == 2  # 2 סיבות עיקריות - Speeding, Distraction

    # נוודא את המספרים
    speeding = next(item for item in result if item['_id'] == "Speeding")
    assert speeding['total_crashes'] == 2

    distraction = next(item for item in result if item['_id'] == "Distraction")
    assert distraction['total_crashes'] == 1


def test_aggregate_injuries_statistics(crash_db_collection):
    pass
