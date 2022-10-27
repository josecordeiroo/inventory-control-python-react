from flask import Blueprint, current_app


routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return 'index'
