from flask import render_template
from core import app

@app.route('/')
def index():
    greeting = "Hello there!"
    return render_template('index.html', greet=greeting)


@app.get('/profile')
def my_profile():
    response_body = {
        "name": "Test",
        "about" :"Hello! Get familiarized with python and javascript"
    }

    return response_body
