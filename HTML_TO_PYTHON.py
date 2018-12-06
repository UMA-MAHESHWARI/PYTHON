from flask import render_template
from flask import Flask
app= Flask(__name__,static_url_path='/static')

@app.route('/<name>/')
def hello(name=None):
    return render_template('username.html')