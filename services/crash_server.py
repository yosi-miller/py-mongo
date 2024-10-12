
from database.connect import get_db
from repository.query_repository import fetch_crash_data_by_period, aggregate_crashes_by_cause, \
    aggregate_injuries_statistics, fetch_crash_by_area
from services.logger import log_info, log_error


def find_crash_by_area(area):
    client, db = get_db()
    try:
        crashs = fetch_crash_by_area(area, db, 'crash information')
        log_info('get all crashs from db')
        return crashs
    except Exception as e:
        log_error(f'action: get all crashs from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()


def find_crash_by_area_and_season(area, date, range_search):
    client, db = get_db()

    try:
        result = fetch_crash_data_by_period(area, date, range_search, db, 'crash information')
        log_info('get crashs from db by area and season')
        return result

    except Exception as e:
        log_error(f'action: get crashs from db by area and season, error: {e}')
        print(f'Error: {e}')
        return e

    finally:
        client.close()

def find_crash_by_group(area):
    client, db = get_db()
    try:
        crashs = aggregate_crashes_by_cause(area, db, 'crash information')
        log_info('get all crashs from db')
        return crashs
    except Exception as e:
        log_error(f'action: get all crashs from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()

def find_injuries_statistics(area):
    client, db = get_db()
    try:
        crashs = aggregate_injuries_statistics(area, db, 'crash information')
        log_info('get all injuries statistics from db')
        return crashs
    except Exception as e:
        log_error(f'action: get all injuries statistics from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()