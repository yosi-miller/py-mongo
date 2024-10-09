from flask import Blueprint, jsonify
from services.users_server import get_all_users

user_bp = Blueprint('user', __name__)

@user_bp.route('/users/')
def get_users():
    # TODO: להכניס לקובץ HTML יפה
    users = get_all_users()
    return jsonify(users), 201 if users else 404