from flask import Blueprint
from .models import Post

post_blp = Blueprint('post_blp', __name__, template_folder='templates/post')

from . import views
