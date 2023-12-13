from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class TodoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    completed = BooleanField('Completed')