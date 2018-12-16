from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def on_load():
    html = render_template('template.html')
    return html

@app.route('/', methods=['POST'])
def after_post():
    text = request.form['text']
    html = render_template('template.html')
    return html + "<p style='color:blue;'>" + text + "</p>"