from flask import Flask, render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, log_out


posts = [
    {
        'author': 'Wilson Peter',
        'title': 'Quote',
        'content': 'Dont just have a love life.LOve life',
        'date_posted': 'SEptember 20, 2020'
    },
    {
        'author': 'Jane Janett',
        'title': 'Inspire',
        'content': 'Practice makes perfect',
        'date_posted': 'September 21, 2020'
    }
]



@app.route('/home')
def home():
    title = 'Memoirs Gram'
    return  render_template('home.html', title = title)

@app.route('/about')
def about():
    return  render_template('about.html', posts = posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! Lets get started', 'success')
        return redirect(url_for('about'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user,remember=form.remember.data)
                return redirect(url_for('about'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
def account():
    return render_template('account.html', title='Account')


