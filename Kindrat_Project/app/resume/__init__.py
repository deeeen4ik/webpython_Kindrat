from flask import Blueprint

resume_bp = Blueprint('resume_bp', __name__, template_folder='templates/resume')

from . import models