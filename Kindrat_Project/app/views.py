from flask import Flask, make_response, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from .forms import ChangePasswordForm, TodoForm, FeedbackForm, RegistrationForm, LoginForm, UpdateAccountForm
from .models import Todo, Feedback, User
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from app import app, db, bcrypt
from PIL import Image
import secrets
import os
import json

my_skills = [
    'Python',
    'JavaScript',
    'HTML',
    'CSS',
    'Flask',
    'SQL',
]

def navigation():
    return {
        'home': 'Home',
        'resume': 'Resume',
        'skill': 'Skills',
        'todos': 'Todo',
        'feedbacks': 'FeedBacks',
        'users': 'Users',
        'info': 'Info',
    }

@app.context_processor
def inject_navigation():
    return dict(navigation=navigation())

def load_users():
    with open('C:\\PNY\\Web-Python_Kindrat\\Kindrat_Project\\app\\configs\\users.json', 'r') as file:
        return json.load(file)
    
def save_users(users):
    with open('C:\\PNY\\Web-Python_Kindrat\\Kindrat_Project\\app\\configs\\users.json', 'w') as file:
        json.dump(users, file, indent=4)

def authenticate(username, password):
    users = load_users()["users"]
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

@app.route('/')
def home():
    os_type = os.name
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('portfolio.html', os_type=os_type, user_agent=user_agent, current_time=current_time)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/skills')
@app.route('/skills/<int:id>')
def skill(id=None):
    if id is None:
        return render_template('skills.html', skills=my_skills)
    elif id >= 0 and id < len(my_skills):
        return f"Skill {id}: {my_skills[id]}"
    else:
        return "Skill not found"
    
@app.route('/register', methods=['GET', 'POST'])
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

@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/info', methods=['GET', 'POST'])
@login_required
def info():
    username = session.get('username')

    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        expiry = request.form.get('expiry')

        if key and value:
            response = make_response(redirect(url_for('info')))
            response.set_cookie(key, value, expires=expiry)
            flash('Cookie added successfully!', 'success')
            return response
        else:
            flash('Key and value are required to add a cookie', 'error')
            return "Key and value are required to add a cookie"

    delete_key = request.args.get('delete_key')
    if delete_key:
        response = make_response(redirect(url_for('info')))
        if delete_key == 'all':
            for key in request.cookies:
                response.delete_cookie(key)
        else:
            response.delete_cookie(delete_key)
        flash('Cookie deleted successfully!', 'success')
        return response

    cookies_info = [(key, request.cookies[key]) for key in request.cookies]
    return render_template('info.html', username=username, cookies_info=cookies_info)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))
    
@app.route('/change_password', methods=['GET', 'POST'])
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

@app.route('/todos', methods=['GET', 'POST'])
def todos():
    form = TodoForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        completed = form.completed.data

        new_todo = Todo(title=title, description=description, completed=completed)
        db.session.add(new_todo)
        db.session.commit()
        flash('Todo added successfully!', 'success')
        return redirect(url_for('todos'))

    todos = Todo.query.all()
    return render_template('todos.html', form=form, todos=todos)

@app.route('/todo/<int:id>', methods=['GET', 'POST'])
def todo(id):
    todo = Todo.query.get_or_404(id)
    form = TodoForm(obj=todo)
    if form.validate_on_submit():
        todo.title = form.title.data
        todo.description = form.description.data
        todo.completed = form.completed.data
        db.session.commit()
        flash('Todo updated successfully!', 'success')
        return redirect(url_for('todos'))
    return render_template('todo.html', form=form, todo=todo)

@app.route('/todo/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for('todos'))

@app.route('/feedbacks', methods=['GET', 'POST'])
def feedbacks():
    feedback_form = FeedbackForm()
    if feedback_form.validate_on_submit():
        username = feedback_form.username.data
        feedback_text = feedback_form.feedback.data

        new_feedback = Feedback(username=username, feedback=feedback_text)
        db.session.add(new_feedback)
        db.session.commit()
        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('feedbacks'))

    feedbacks = Feedback.query.all()
    return render_template('feedbacks.html', feedback_form=feedback_form, feedbacks=feedbacks)

@app.route('/users')
@login_required
def users():
    all_users = User.query.all()
    total_users = len(all_users)
    return render_template('users.html', all_users=all_users, total_users=total_users)

@app.route('/account', methods=['GET', 'POST'])
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
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)

    current_user.image_file = picture_fn
    db.session.commit()

    return picture_fn

@app.after_request
def after_request(response):
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        try:
            db.session.commit()
        except:
            flash('Error while updating user last seen!', 'danger')
    return response