from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name: str):
    app = Flask(__name__)
    
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
        app.register_blueprint(todo)
        app.register_blueprint(feedback)
        app.register_blueprint(portfolio)
        app.register_blueprint(auth)
        app.register_blueprint(users)
        app.register_blueprint(info)
        
        return app 