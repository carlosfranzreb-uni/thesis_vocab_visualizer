from flask import render_template

from app import app, utils
from app.forms import MainForm


@app.route("/", methods=['GET','POST'])
def home():
    form = MainForm()
    title, abstract = '', ''
    if form.is_submitted():
        title, abstract = utils.get_doc(form.id.data)
    return render_template(
      'main.html',
      title=title,
      abstract=abstract,
      form=form
    )
