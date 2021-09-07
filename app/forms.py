from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField


class MainForm(FlaskForm):
    id = StringField()
    vocab = SelectField(choices=['Unfiltered', 'Step 1', 'Step 2', 'Step 4'])
    submit = SubmitField('Submit')