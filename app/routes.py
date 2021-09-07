
import json
from flask import render_template

from app import app, utils
from app.forms import MainForm


@app.route("/", methods=['GET','POST'])
def home():
    form = MainForm()
    title_marked, abstract_marked = 'Title', 'Abstract'
    if form.is_submitted():
    vocab = utils.get_vocab(form.vocab.data)
    return render_template(
      'main.html',
      title=title_marked,
      abstract=abstract_marked,
      form=form
    )
