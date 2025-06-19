from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("Planet_Story")

@app.route("/")
def main():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)
