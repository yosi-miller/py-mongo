def crash_document(row):
    crash_cause = {
        'prim': row['PRIM_CONTRIBUTORY_CAUSE'],
        'sec': row['SEC_CONTRIBUTORY_CAUSE']
    }

    injuries_info = {
        'total': row['INJURIES_TOTAL'],
        'injuries_status': {
            'fatal': row['INJURIES_FATAL'],
            'incapacitating': row['INJURIES_INCAPACITATING'],
            'non incapacitating': row['INJURIES_NON_INCAPACITATING']
        }
    }
    crash = {
        'date': row['CRASH_DATE'],
        'beat': row['BEAT_OF_OCCURRENCE'],
        'day of week': row['CRASH_DAY_OF_WEEK'],
        'month': row['CRASH_MONTH'],
        'crash_cause': crash_cause,
        'injuries_info': injuries_info
    }

    return crash

