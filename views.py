from flask import Flask, render_template, url_for, redirect
from app import app

app = Flask(__name__)


@app.route('/')
def home():
    return  render_template('Home.html')

@app.route('/')
def about():
    return  render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
