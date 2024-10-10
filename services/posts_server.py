from database.connect import get_db
from services.logger import log_info, log_error


def find_crash_by_area(area):
    client, db = get_db()
    print(area)
    try:
        crashs = list(db['crash information'].find({'beat': area}, {'_id': 0, 'injuries_info': 0}))
        print(crashs)
        log_info('get all crashs from db')
        return crashs
    except Exception as e:
        log_error(f'action: get all crashs from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()


def find_crash_by_area_and_season(area, season):
    client, db = get_db()

    try:
        print('get all crash')
        crashs = list(db['crash information'].find({'bead': area,'season': season}, {'_id': 0}))
        # users = list(db.posts.find({'userId': user_id}, {'_id': 0}))
        # log_info('get all users posts_by_user_id from db')
        return crashs
    except Exception as e:
        # log_error(f'action: get all users posts_by_user_id from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()

def find_crash_by_group():
    pass

def find_injuries_statistics():
    pass