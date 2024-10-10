from datetime import datetime, timedelta

from database.connect import get_db
from services.logger import log_info, log_error


def find_crash_by_area(area):
    client, db = get_db()
    try:
        crashs = list(db['crash information'].find({'beat': area}, {'_id': 0, 'injuries_info': 0}))
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
    # TODO:לחלק את השאלתיה ל 2 חלקים
    try:
        time_periods = {
            "day": 1,
            "week": 7,
            "month": 30
        }

        add_date = time_periods.get(range_search)

        start_date = datetime.strptime(date, '%m-%d-%Y')
        end_date = start_date + timedelta(days=add_date)

        sum_crash = db['crash information'].count_documents(
            {'beat': area,
             "date": {"$gte": start_date, "$lt": end_date}})

        result = {
            "start_date": start_date,
            "end_date": end_date,
            "area": area,
            "range_search": range_search,
            "total_crashes": sum_crash
        }

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
        crashs = list(db['crash information'].aggregate([
        {
            '$match': {
                'beat': area
            }
        },
        {
            '$group': {
                '_id': '$crash_cause.prim',
                'total_crashes': {'$sum': 1}
            }
        }
        ]))
        log_info('get all crashs from db')
        return crashs
    except Exception as e:
        log_error(f'action: get all crashs from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()

def find_injuries_statistics():
    pass