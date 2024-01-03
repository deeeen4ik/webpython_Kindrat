from datetime import datetime, timedelta
from flask import make_response, request, jsonify, request
from flask_jwt_extended import jwt_required
from . import api_bp
from app import db, basic_auth
from config import Config
from app.auth.models import User
from app.todo.models import Todo
from app.resume.models import Resume
import jwt

@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return True
    return False

@api_bp.route('/login')
def login():
    auth = request.authorization

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('No such user in database', 401, {'WWW-Authenticate': 'Bearer realm="Authentication Required"'}) 

    if user.password == auth.password:
        expiry = datetime.utcnow() + timedelta(minutes=30)
        subject = "access"
        secret_key = Config.SECRET_KEY

        token = jwt.encode(
            {"sub": subject, "username": user.username, "exp": expiry},
            secret_key, 
            algorithm="HS256"
        )

        return jsonify({"token": token})

    return make_response('Invalid username or password', 401, {'WWW-Authenticate': 'Bearer realm="Authentication Required"'})






@api_bp.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    todos = Todo.query.all()
    todo_list = [{'id': todo.id, 'title': todo.title, 'description': todo.description, 'completed': todo.completed} for todo in todos]
    return jsonify({'todos': todo_list})

@api_bp.route('/todos', methods=['POST'])
@jwt_required()
def create_todo():
    data = request.json
    new_todo = Todo(title=data['title'], description=data.get('description'), completed=data.get('completed', False))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'}), 201

@api_bp.route('/todos/<int:id>', methods=['GET'])
@jwt_required()
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify({'id': todo.id, 'title': todo.title, 'description': todo.description, 'completed': todo.completed})

@api_bp.route('/todos/<int:id>', methods=['PUT'])
@jwt_required()
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.json
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify({'message': 'Todo updated successfully'}), 200

@api_bp.route('/todos/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'}), 200




@api_bp.route('/resumes', methods=['GET'])
@jwt_required()
def get_resumes():
    resumes = Resume.query.all()
    resume_list = []
    for resume in resumes:
        resume_list.append({
            'id': resume.id,
            'title': resume.title,
            'description': resume.description,
            'skills': resume.skills
        })
    return jsonify({'resumes': resume_list})

@api_bp.route('/resumes', methods=['POST'])
@jwt_required()
def create_resume():
    data = request.json
    new_resume = Resume(
        title=data.get('title'),
        description=data.get('description'),
        skills=data.get('skills')
    )
    db.session.add(new_resume)
    db.session.commit()
    return jsonify({'message': 'Resume created successfully'}), 201

@api_bp.route('/resumes/<int:id>', methods=['GET'])
@jwt_required()
def get_resume(id):
    resume = Resume.query.get_or_404(id)
    return jsonify({
        'id': resume.id,
        'title': resume.title,
        'description': resume.description,
        'skills': resume.skills
    })

@api_bp.route('/resumes/<int:id>', methods=['PUT'])
@jwt_required()
def update_resume(id):
    resume = Resume.query.get_or_404(id)
    data = request.json
    resume.title = data.get('title', resume.title)
    resume.description = data.get('description', resume.description)
    resume.skills = data.get('skills', resume.skills)
    db.session.commit()
    return jsonify({'message': 'Resume updated successfully'}), 200

@api_bp.route('/resumes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_resume(id):
    resume = Resume.query.get_or_404(id)
    db.session.delete(resume)
    db.session.commit()
    return jsonify({'message': 'Resume deleted successfully'}), 200