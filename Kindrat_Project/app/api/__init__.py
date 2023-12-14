from flask import Blueprint

todo_api = Blueprint('todo_api', __name__, url_prefix='/api')