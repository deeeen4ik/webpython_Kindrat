from wtforms import BooleanField, FileField, StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from .models import PostType

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    postType = SelectField("Post type (select one)", choices=[
        ('PUBLICATION', "Publication"), ('NEWS', 'News'), ('MEMES', 'Memes'),
        ('SPORT', 'Sport'), ('OTHER', 'Other')
    ])
    enabled = BooleanField('Enabled')
    image = FileField('Add post image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')
