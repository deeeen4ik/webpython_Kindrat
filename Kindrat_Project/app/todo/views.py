from flask import flash, redirect, render_template, url_for
from app import db, navigation
from .forms import TodoForm
from .models import Todo
from . import todo

@todo.context_processor
def inject_navigation():
    return dict(navigation=navigation())

@todo.route('/todos', methods=['GET', 'POST'])
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
        return redirect(url_for('todo.todos'))

    todos = Todo.query.all()
    return render_template('todos.html', form=form, todos=todos)

@todo.route('/todo/<int:id>', methods=['GET', 'POST'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    form = TodoForm(obj=todo)
    if form.validate_on_submit():
        todo.title = form.title.data
        todo.description = form.description.data
        todo.completed = form.completed.data
        db.session.commit()
        flash('Todo updated successfully!', 'success')
        return redirect(url_for('todo.todos'))
    return render_template('todo.html', form=form, todo=todo)

@todo.route('/todo/delete/<int:id>')
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for('todo.todos'))