from flask import render_template, request, redirect, url_for, session, flash
from .forms import ChangePasswordForm, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required
from .handler.account_handler import change_account_image
from app import db, bcrypt, navigation
from datetime import datetime
from .models import User
from . import auth
import json


@auth.context_processor
def inject_navigation():
    return dict(navigation=navigation())

def load_users():
    with open('C:\\PNY\\Web-Python_Kindrat\\Kindrat_Project\\app\\users.json', 'r') as file:
        return json.load(file)
    
def save_users(users):
    with open('C:\\PNY\\Web-Python_Kindrat\\Kindrat_Project\\app\\users.json', 'w') as file:
        json.dump(users, file, indent=4)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_user or existing_email:
            flash('Username or email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('portfolio.home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('portfolio.home'))
    
@auth.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if 'username' in session:
            new_password = form.new_password.data
            if new_password:
                users = load_users()
                for user in users['users']:
                    if user['username'] == session['username']:
                        user['password'] = new_password

                save_users(users)
                flash('Password changed successfully!', 'success')
                return redirect(url_for('auth.login'))
            else:
                flash('New password is required to change', 'error')
                return redirect(url_for('auth.change_password'))

    return render_template('change_password.html', form=form)

@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    update_form = UpdateAccountForm()
    if update_form.validate_on_submit():
        current_user.username = update_form.username.data
        current_user.email = update_form.email.data
        current_user.about_me = update_form.about_me.data
        
        if update_form.profile_picture.data:
            picture_file = change_account_image(update_form.profile_picture.data)
            current_user.image_file = picture_file
        
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        update_form.username.data = current_user.username
        update_form.email.data = current_user.email
        update_form.about_me.data = current_user.about_me
    return render_template('account.html', title='Account', current_user=current_user, update_form=update_form)


@auth.after_request
def after_request(response):
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        try:
            db.session.commit()
        except:
            flash('Error while updating user last seen!', 'danger')
    return response