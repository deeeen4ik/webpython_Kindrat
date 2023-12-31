from flask import url_for
from flask_login import current_user
from app.auth.models import User
from app import db


def test_register_user(client):
    response = client.post(
        url_for('auth.register'),
        data=dict(
            username='test1',
            email='test1@gmail.com',
            password='1234',
            confirm_password='1234'
        ),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'Your account has been created!' in response.data


def test_login_user(client):
    response = client.post(
        url_for('auth.login', external=True),
        data=dict(
            username='test1',
            password='1234'
        ),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"You have been logged in!" in response.data
    

def test_log_out_user(client, log_in_default_user):
    response = client.get(
        url_for('auth.logout'),
        follow_redirects = True
    )
    
    assert b'You have been logged out', response.data
    assert response.status_code == 200
    assert current_user.is_authenticated == False