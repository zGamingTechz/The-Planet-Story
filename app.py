from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask("Planet_Story")

@app.route("/")
def title_screen():
    return render_template("title.html")

if __name__ == "__main__":
    app.run(debug=True)
