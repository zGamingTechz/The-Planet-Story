from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("Planet_Story")


@app.route("/", methods=["GET", "POST"])
def title_screen():
    if request.method == "POST":
        return "Home"
    return render_template("title.html")


if __name__ == "__main__":
    app.run(debug=True)
