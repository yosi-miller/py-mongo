from flask import Blueprint, jsonify
from configuration_db import get_db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users/')
def get_users():
    # TODO: להכניס לקובץ HTML יפה
    client, db = get_db()
    users = list(db.users.find({}, {'_id': 0}))
    client.close()
    return jsonify(users), 201