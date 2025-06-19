from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask("Planet_Story")


@app.route("/", methods=["GET", "POST"])
def title_screen():
    if request.method == "POST":
        return redirect("/home")
    return render_template("title.html")


@app.route("/home", methods=["GET", "POST"])
def home_screen():
    return render_template("home.html")

@app.route('/')
def home():
    return render_template('index.html')
@app.route("/jupiter", methods=["GET", "POST"])
def jupiter_story():
    return render_template("jupiter.html")

@app.route("/earth", methods=["GET", "POST"])
def earth_story():
    return render_template("earth.html")

@app.route("/mars", methods=["GET", "POST"])
def mars_story():
    return render_template("mars.html")

@app.route("/mercury", methods=["GET", "POST"])
def mercury_story():
    return render_template("mercury.html")

@app.route("/neptune", methods=["GET", "POST"])
def neptune_story():
    return render_template("neptune.html")

@app.route("/pluto", methods=["GET", "POST"])
def pluto_story():
    return render_template("pluto.html")

@app.route("/saturn", methods=["GET", "POST"])
def saturn_story():
    return render_template("saturn.html")

@app.route("/uranus", methods=["GET", "POST"])
def uranus_story():
    return render_template("uranus.html")

@app.route("/venus", methods=["GET", "POST"])
def venus_story():
    return render_template("venus.html")



if __name__ == "__main__":
    app.run(debug=True)
