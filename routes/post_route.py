from flask import Blueprint, jsonify
from configuration_db import get_db

post_bp = Blueprint('post', __name__)


@post_bp.route('/posts/')
def get_posts():
    client, db = get_db()
    users = list(db.posts.find({}, {'_id': 0}))
    client.close()
    return jsonify(users), 201

@post_bp.route('/posts/<int:user_id>', methods=['GET'])
def get_posts_by_id(user_id):
    client, db = get_db()
    posts = list(db.posts.find({'userId': user_id}, {'_id': 0}))
    client.close()
    return jsonify(posts), 201