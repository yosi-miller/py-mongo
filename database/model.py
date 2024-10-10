from datetime import datetime


def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)


def injuries_info(row):
    injuries = {
        'total': row['INJURIES_TOTAL'],
        'injuries_status': {
            'fatal': row['INJURIES_FATAL'],
            'incapacitating': row['INJURIES_INCAPACITATING'],
            'non_incapacitating': row['INJURIES_NON_INCAPACITATING']
        }
    }

    return injuries


def crash_document(row, injuries_info_id):
    crash_cause = {
        'prim': row['PRIM_CONTRIBUTORY_CAUSE'],
        'sec': row['SEC_CONTRIBUTORY_CAUSE']
    }

    crash = {
        'date': parse_date(row['CRASH_DATE']),
        'beat': row['BEAT_OF_OCCURRENCE'],
        'day_of_week': row['CRASH_DAY_OF_WEEK'],
        'month': row['CRASH_MONTH'],
        'crash_cause': crash_cause,
        'injuries_info': injuries_info_id
    }

    return crash

if __name__ == '__main__':
    t = parse_date('09/22/2023 06:45:00 PM')
    print(type(t))
