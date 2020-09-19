from flask import Flask,render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return  render_template('Home.html')

@app.route('/about')
def about():
    return  render_template('about.html')