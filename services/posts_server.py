from repository.insert_data_db import get_db
from services.logger import log_info, log_error


def get_all_posts():
    client, db = get_db()

    try:
        users = list(db.posts.find({}, {'_id': 0}))
        log_info('get all posts from db')
        return users
    except Exception as e:
        log_error(f'action: get all posts from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()


def get_posts_by_user_id(user_id):
    client, db = get_db()

    try:
        users = list(db.posts.find({'userId': user_id}, {'_id': 0}))
        log_info('get all users posts_by_user_id from db')
        return users
    except Exception as e:
        log_error(f'action: get all users posts_by_user_id from db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()