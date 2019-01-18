from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to the world!"

@app.route('/user')
def user():
    return "Welcome to user page!"