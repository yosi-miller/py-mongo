from flask import Blueprint, jsonify, request
from services.crash_server import find_crash_by_area, find_crash_by_area_and_season, find_crash_by_group, find_injuries_statistics

crash_bp = Blueprint('post', __name__, url_prefix='/crash')

@crash_bp.route('/area/<string:area>/')
def get_crash_by_area(area):
    area = find_crash_by_area(area)
    return jsonify(area), 201 if len(area) > 1 else 404

@crash_bp.route('/season/<string:area>/<string:date>/<string:range_search>/', methods=['GET'])
def get_crash_by_area_and_season(area, date, range_search):
    posts = find_crash_by_area_and_season(area, date, range_search)
    return jsonify(posts), 201 if posts else 404


@crash_bp.route('/group/<string:area>/', methods=['GET'])
def get_crash_by_group(area):
    posts = find_crash_by_group(area)
    return jsonify(posts), 201 if posts else 404

#  Statistics on injuries
@crash_bp.route('/injuries_statistics/<string:area>/', methods=['GET'])
def get_injuries_statistics(area):
    stats = find_injuries_statistics(area)
    return jsonify(stats), 201 if stats else 404

# TODO: לבדוק מה חוזר אם יש מידע ריק

query = 3