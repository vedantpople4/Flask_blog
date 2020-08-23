from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Aman Dhatterwal',
        'title':'Blog on Flutter',
        'content':'First blog post on flutter',
        'date_posted':'August 15, 2020'
    },
    {
        'author': 'Love Babbar',
        'title':'Blog on Machine Learning',
        'content':'First blog post on ML',
        'date_posted':'August 16, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def hello():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {{form.username.data}}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check Username and password','danger')

    return render_template('login.html',title='=Login', form=form)

