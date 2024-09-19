from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def homepage():
    movies = [
        {"title": "Film 1"},
        {"title": "Film 2"},
        {"title": "Film 3"},
        {"title": "Film 4"},
    ]
    return render_template("homepage.html", movies=movies)