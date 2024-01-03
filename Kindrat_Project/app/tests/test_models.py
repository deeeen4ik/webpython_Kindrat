from .base import BaseTestCase
from app.auth.models import User
from app.todo.models import Todo                                                     


class ModelTests(BaseTestCase):
    
    def test_user_model(self):
        """
        GIVEN  a user model
        WHEN a new user is created 
        THEN check the email and password fields are defined correctly
        """
        
        user = User(username = "user", email = "user@gmail.com", password = "pasw")
        assert user.username == 'user'
        assert user.email == 'user@gmail.com'
        assert user.password == 'pasw'
        
        
    def test_todo_model(self):
        """
        GIVEN  a todo model
        WHEN a new todo is created 
        THEN check the title and description fields are defined correctly
        """
        
        todo = Todo(title = "todo title", description = "this is todo description")
        assert todo.title == "todo title"
        assert todo.description == "this is todo description"