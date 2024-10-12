from repository.query_repository import fetch_crash_data_by_period, aggregate_crashes_by_cause, \
    aggregate_injuries_statistics, fetch_crash_by_area
from tests.conftest import crash_db_collection, populate_crash_db


def test_insert_crash(crash_db_collection, populate_crash_db):
    assert crash_db_collection.count_documents({}) > 1
    assert crash_db_collection.count_documents({}) == 27

# WARRING: from hear writer with gpt
def test_find_crash_by_area(init_db, populate_crash_db):
    # הכנת נתוני בדיקה
    test_area = "422"

    result = fetch_crash_by_area(test_area, init_db, 'crash_test')

    assert isinstance(result, list), "The result should be a list"
    assert len(result) > 0, f"No crashes found for area {test_area}"

def test_fetch_crash_data_by_period(init_db, populate_crash_db):
    # Test for a specific day
    result = fetch_crash_data_by_period("422", "11-11-2023", "day", init_db, 'crash_test')
    assert result["total_crashes"] == 2
    assert result["range_search"] == "day"
    assert result["area"] == "422"
    assert (result["end_date"] - result["start_date"]).days == 1

    # Test for a week
    result = fetch_crash_data_by_period("422", "11-22-2023", "week", init_db, 'crash_test')
    assert result["total_crashes"] > 0
    assert result["range_search"] == "week"
    assert (result["end_date"] - result["start_date"]).days == 7

    # Test for a month
    result = fetch_crash_data_by_period("422", "11-11-2023", "month", init_db, 'crash_test')
    assert result["total_crashes"] > 0
    assert result["range_search"] == "month"
    assert (result["end_date"] - result["start_date"]).days == 30


def test_aggregate_crashes_by_cause(init_db, populate_crash_db):
    result = aggregate_crashes_by_cause("422", init_db, 'crash_test')

    assert len(result) > 0

    # Check if the result is properly formatted
    for item in result:
        assert '_id' in item
        assert 'total_crashes' in item
        assert isinstance(item['total_crashes'], int)

    # Check if the total crashes match the sum of individual causes
    total_crashes = sum(item['total_crashes'] for item in result)
    db_total = init_db['crash_test'].count_documents({'beat': '422'})
    assert total_crashes == db_total


def test_aggregate_injuries_statistics(init_db, populate_crash_db):
    result = aggregate_injuries_statistics("422", init_db, 'crash_test')

    assert len(result) == 1  # Should return one aggregated result

    injuries = result[0]
    assert 'total_injuries' in injuries
    assert 'fatal_injuries' in injuries
    assert 'incapacitating' in injuries
    assert 'non_incapacitating' in injuries

    # Check if the total injuries is the sum of the other categories
    total = injuries['fatal_injuries'] + injuries['incapacitating'] + injuries['non_incapacitating']
    assert injuries['total_injuries'] == total

    # Ensure all injury counts are non-negative
    for key, value in injuries.items():
        if key != '_id':
            assert value >= 0