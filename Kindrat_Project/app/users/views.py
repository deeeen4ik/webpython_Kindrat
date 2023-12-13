from flask import render_template
from flask_login import login_required
from auth.models import User
from . import users

@users.route('/users')
@login_required
def user():
    all_users = User.query.all()
    total_users = len(all_users)
    return render_template('users.html', all_users=all_users, total_users=total_users)