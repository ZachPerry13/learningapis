# routes/api.py
from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'This is JSON data from the API'}
    return jsonify(data)
