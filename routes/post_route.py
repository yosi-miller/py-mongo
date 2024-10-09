from flask import Blueprint, jsonify
from services.posts_server import get_all_posts, get_posts_by_user_id

post_bp = Blueprint('post', __name__)

@post_bp.route('/posts/')
def get_posts():
    users = get_all_posts()
    return jsonify(users), 201 if users else  400

@post_bp.route('/posts/<int:user_id>', methods=['GET'])
def get_posts_by_id(user_id):
    posts = get_posts_by_user_id(user_id)
    return jsonify(posts), 201 if posts else  404