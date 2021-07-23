from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class MainForm(FlaskForm):
    doi = StringField()
    submit = SubmitField('Submit')