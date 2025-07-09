from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    movies = []
    return render_template("homepage.html", movies=range(8))


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
