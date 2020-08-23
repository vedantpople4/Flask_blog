from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm
from models import User,Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f021fcff13fe1e30aa8436ec92d8449c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



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


if __name__ == '__main__':
    app.run(debug=True)

