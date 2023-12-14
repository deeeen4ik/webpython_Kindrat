from flask import request, jsonify, request
from . import todo_api
from app import db
from app.todo.models import Todo

@todo_api.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todo_list = [{'id': todo.id, 'title': todo.title, 'description': todo.description, 'completed': todo.completed} for todo in todos]
    return jsonify({'todos': todo_list})

@todo_api.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    new_todo = Todo(title=data['title'], description=data.get('description'), completed=data.get('completed', False))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'}), 201

@todo_api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify({'id': todo.id, 'title': todo.title, 'description': todo.description, 'completed': todo.completed})

@todo_api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.json
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify({'message': 'Todo updated successfully'}), 200

@todo_api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'}), 200