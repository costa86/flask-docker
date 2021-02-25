from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    post = TextAreaField("Your post",validators=[DataRequired(),Length(min=5,max=140)])
    submit = SubmitField("Publish")