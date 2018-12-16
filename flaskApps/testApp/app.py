# run with cmmand: FLASK_APP=app.py flask run

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def on_load():
    html = render_template('template.html', name='')
    return html

@app.route('/', methods=['POST'])
def after_post():
    text = request.form['text']
    html = render_template('template.html', name=text)
    return html