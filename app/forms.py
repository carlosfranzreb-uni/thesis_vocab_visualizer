from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class MainForm(FlaskForm):
    id = StringField()
    submit = SubmitField('Submit')