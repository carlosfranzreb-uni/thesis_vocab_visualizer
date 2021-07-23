from flask import render_template, url_for, redirect, send_file
import os.path
import sys

from app import app, utils
from app.forms import MainForm


@app.route("/", methods=['GET','POST'])
def home():
    form = MainForm()
    tasks_output, trucks_output = '', ''
    if form.is_submitted():
        tasks = utils.parse_tasks(form.tasks.data)
        trucks = utils.parse_trucks(form.trucks.data)
        # TODO (ELias): init tasks and truck objects.
        # TODO (Elias): create tuples to be displayed.
        # TODO (Elias): transform tuples back to string.
        tasks_output = '1,2,3\n1,2,3'
        trucks_output = '1,2,3\n1,2,3'
    return render_template(
      'main.html',
      title='Home',
      form=form,
      tasks=tasks_output,
      trucks=trucks_output
    )


@app.route("/output")
def output():
    compute("input.wav", "hls/output.wav")
    return send_file("output.wav")