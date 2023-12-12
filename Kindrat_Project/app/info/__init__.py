from flask import Blueprint

info = Blueprint('info', __name__, template_folder='templates/info')

from . import views
