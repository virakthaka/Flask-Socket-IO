from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    data = {'message': 'Welcome to the world!'}
    return render_template('index.html', title='HomePage', data=data)

@app.route('/user')
def user():
    return "Welcome to user page!"