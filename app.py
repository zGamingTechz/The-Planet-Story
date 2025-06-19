from flask import Flask, render_template, request, redirect, jsonify
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


@app.route("/jupiter", methods=["GET", "POST"])
def jupiter_story():
    story = [
        "Part 1",
        "Part 2",
        "Part 3",
        "Part 4",
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("jupiter.html", story = story[0])


if __name__ == "__main__":
    app.run(debug=True)
