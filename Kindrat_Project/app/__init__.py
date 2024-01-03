from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
from config import config

# bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()

def navigation():
    return {
        'portfolio.home': 'Home',
        'portfolio.resume': 'Resume',
        'portfolio.skill': 'Skills',
        'todo.todos': 'Todo',
        'feedback.feedbacks': 'FeedBacks',
        'users.user': 'Users',
        'info.infos': 'Info',
        'post_blp.posts': 'Posts',
    }

def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))

    db.init_app(app)
    Migrate(app, db)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    with app.app_context():
        from .todo.views import todo
        from .feedback.views import feedback
        from .portfolio.views import portfolio
        from .auth.views import auth
        from .users.views import users
        from .info.views import info
        from .api.todo import todo_api
        from .posts.views import post_blp
        app.register_blueprint(todo)
        app.register_blueprint(feedback)
        app.register_blueprint(portfolio)
        app.register_blueprint(auth)
        app.register_blueprint(users)
        app.register_blueprint(info)
        app.register_blueprint(todo_api)
        app.register_blueprint(post_blp)
        
        return app 