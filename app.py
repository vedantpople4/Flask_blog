from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)

