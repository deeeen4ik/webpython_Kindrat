from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from .forms import ChangePasswordForm, RegistrationForm, LoginForm, UpdateAccountForm
from .models import User
from flask_login import login_user, current_user, logout_user, login_required
from . import auth
from app import db, bcrypt
from PIL import Image
import secrets
import json
import os

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
            return redirect(url_for('register'))
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))
    
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
                return redirect(url_for('login'))
            else:
                flash('New password is required to change', 'error')
                return redirect(url_for('change_password'))

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
            picture_file = save_profile_picture(update_form.profile_picture.data)
            current_user.image_file = picture_file
        
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        update_form.username.data = current_user.username
        update_form.email.data = current_user.email
        update_form.about_me.data = current_user.about_me
    return render_template('account.html', title='Account', current_user=current_user, update_form=update_form)

def save_profile_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(auth.root_path, 'static/images', picture_fn)

    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)

    current_user.image_file = picture_fn
    db.session.commit()

    return picture_fn

@auth.after_request
def after_request(response):
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        try:
            db.session.commit()
        except:
            flash('Error while updating user last seen!', 'danger')
    return response