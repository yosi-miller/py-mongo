from datetime import datetime


def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)


def injuries_info(row):
    injuries = {
        'total': 0 if row['INJURIES_TOTAL'] == '' else int(row['INJURIES_TOTAL']),
        'fatal': 0 if row['INJURIES_FATAL'] == '' else int(row['INJURIES_FATAL']),
        'incapacitating': 0 if row['INJURIES_INCAPACITATING'] == '' else int(row['INJURIES_INCAPACITATING']),
        'non_incapacitating': 0 if row['INJURIES_NON_INCAPACITATING'] == '' else int(row['INJURIES_NON_INCAPACITATING'])
    }

    return injuries


def crash_document(row, injuries):
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
        'injuries_info': injuries
    }

    return crash
