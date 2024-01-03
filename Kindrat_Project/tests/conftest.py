from flask import url_for
import pytest
from app import create_app, db
from app.auth.models import User
from app.posts.models import Post

@pytest.fixture(scope='module')
def client():
    app = create_app('test')
    app.config['SERVER_NAME'] = '127.0.0.1:5000'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

@pytest.fixture()
def user_test():
    user = User(username='user1', email='user1@gmail.com', password='1234')
    return user

@pytest.fixture(scope='module')
def init_database(client):
    default_user = User(username='default', email='default@gmail.com', password='1234')
    post_1 = Post(title="Post1", text='Post1', user_id=1)
    post_2 = Post(title="Post2", text='Post2', user_id=1)
    db.session.add(default_user)
    db.session.add(post_1)
    db.session.add(post_2)
    db.session.commit()

    yield

@pytest.fixture(scope='function')
def log_in_default_user(client):
    client.post(url_for('auth.login'),
                     data=dict(username='default', password='1234'),
                     follow_redirects=True
                     )

    yield 

    client.get(url_for('auth.logout'))