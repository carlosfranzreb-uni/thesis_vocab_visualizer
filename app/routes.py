
import json
from flask import render_template

from app import app, utils
from app.forms import MainForm


@app.route("/", methods=['GET','POST'])
def home():
    form = MainForm()
    title, abstract = '', ''
    if form.is_submitted():
      title, abstract = utils.get_doc(form.id.data)
      vocab = json.load(open('app/static/data/vocab/repo_vocab.json'))
      title_words = utils.get_vocab_words(title, vocab)
      title_marked = utils.format_text(title_words)
      abstract_words = utils.get_vocab_words(abstract, vocab)
      abstract_marked = utils.format_text(abstract_words)
    return render_template(
      'main.html',
      title=title_marked,
      abstract=abstract_marked,
      form=form
    )
