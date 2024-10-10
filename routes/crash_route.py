from flask import Blueprint, jsonify, request
from services.posts_server import find_crash_by_area, find_crash_by_area_and_season, find_crash_by_group, find_injuries_statistics

crash_bp = Blueprint('post', __name__, url_prefix='/crash')

@crash_bp.route('/area/<string:area>/')
def get_crash_by_area(area):
    users = find_crash_by_area(area)
    return jsonify(users), 201 if users else 404


@crash_bp.route('/season/<string:area>/', methods=['GET'])
def get_crash_by_area_and_season(area):
    season = request.json()
    posts = find_crash_by_area_and_season(area, season)
    return jsonify(posts), 201 if posts else 404


@crash_bp.route('/group/', methods=['GET'])
def get_crash_by_group():
    posts = find_crash_by_group()
    return jsonify(posts), 201 if posts else 404

#  Statistics on injuries
@crash_bp.route('/injuries_statistics/', methods=['GET'])
def get_injuries_statistics():
    stats = find_injuries_statistics()
    return jsonify(stats), 201 if stats else 404