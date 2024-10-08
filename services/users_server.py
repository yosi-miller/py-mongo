from configuration_db import get_db
from services.logger import log_info, log_error


def get_all_users():
    client, db = get_db()

    try:
        users = list(db.users.find({}, {'_id': 0}))
        log_info('get all users from db')
        return users
    except Exception as e:
        log_error(f'action: get all users from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()