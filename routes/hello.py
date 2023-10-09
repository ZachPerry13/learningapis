# routes/hello.py
from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello')

def hello_world():
    return 'Hello, World!'
