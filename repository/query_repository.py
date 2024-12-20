from datetime import datetime, timedelta


def fetch_crash_by_area(area, db, col_name):
    crashs = list(db[col_name].find({'beat': area}, {'_id': 0}))
    return crashs

def fetch_crash_data_by_period(area, date, range_search, db, col_name):
    time_periods = {
        "day": 1,
        "week": 7,
        "month": 30
    }

    add_date = time_periods.get(range_search)

    start_date = datetime.strptime(date, '%m-%d-%Y')
    end_date = start_date + timedelta(days=add_date)

    sum_crash = db[col_name].count_documents(
        {'beat': area,
         "date": {"$gte": start_date, "$lt": end_date}})

    result = {
        "start_date": start_date,
        "end_date": end_date,
        "area": area,
        "range_search": range_search,
        "total_crashes": sum_crash
    }
    return result

def aggregate_crashes_by_cause(area, db, col_name):
    result = list(db[col_name].aggregate([
        {'$match': {'beat': area}},
        {'$group': {
            '_id': '$crash_cause.prim',
            'total_crashes': {'$sum': 1}}}
    ]))

    return result

def aggregate_injuries_statistics(area, db, col_name):
    result = list(db[col_name].aggregate([
        {'$match': {'beat': area}},
        {'$group': {
            '_id': None,
            "total_injuries": {"$sum": "$injuries_info.total"},
            "fatal_injuries": {"$sum": "$injuries_info.fatal"},
            "incapacitating": {"$sum": "$injuries_info.incapacitating"},
            "non_incapacitating": {"$sum": "$injuries_info.non_incapacitating"}
        }}
    ]))

    return result