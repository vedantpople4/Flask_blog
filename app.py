from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f021fcff13fe1e30aa8436ec92d8449c'

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='=Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

