from flask import render_template, url_for, redirect
from app import app
from forms import RegistrationForm, LoginForm




@app.route('/')
def home():
    title = 'Memoirs Gram'
    return  render_template('home.html', title = title)

@app.route('/')
def about():
    return  render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_sumit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form='Form')


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data =='password':
            flash('You have been logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful.Please check username and password', 'danger')
    return render_template('login.html', title='Login', form='Form')



