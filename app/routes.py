
import json
from flask import render_template

from app import app, utils
from app.forms import MainForm


@app.route("/", methods=['GET','POST'])
def home():
  form = MainForm()
  title_marked, abstract_marked = 'Title', 'Abstract'
  if form.is_submitted():
    doc = utils.get_doc(form.id.data)
    vocab = utils.get_vocab(form.vocab.data)
    title_words = utils.get_vocab_words(doc['title']['lemmas'], vocab)
    title_marked = utils.format_text(doc['title']['tokens'], title_words)
    abstract_words = utils.get_vocab_words(doc['abstract']['lemmas'], vocab)
    abstract_marked = utils.format_text(doc['abstract']['tokens'], abstract_words)
  return render_template(
    'main.html',
    title=title_marked,
    abstract=abstract_marked,
    form=form
  )
