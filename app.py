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
        "Narrator: Far beyond Mars, in the cold reaches of space, Jupiter watches the little blue world spin.",
        "Jupiter: (soft chuckle) Always so full of life... You really are something, Earth.",
        "Jupiter: (a bit louder) Earth! You look radiant today! Everything alright?",
        "Earth: (short) Fine. Please don’t start.",
        "Jupiter: (pauses, confused) Oh... alright. Just saying hi.",
        "Jupiter: (to himself) She barely looks at me anymore. Did... I do something wrong?",
        "Jupiter: (trying again) I saw those clouds forming near your equator. Need a hand balancing them?",
        "Earth: (sharp) I don’t need help. Especially not from *you*.",
        "Jupiter: (hurt) Oh... okay. Got it.",
        "Jupiter: (quietly) When did she start sounding so... distant?",
        "Narrator: Jupiter turns slowly, his swirling storms hiding a storm within.",
        "Jupiter: (muttering) I’ve done nothing but watch over her... I don’t understand.",
        "Jupiter: (glancing to the side) Maybe Saturn knows something. He always sees what I miss.",
        "Jupiter: (calling out) Saturn? Hey, you awake over there?",
        "Saturn: (gently) I don’t sleep, brother. Just... rotate slowly.",
        "Jupiter: (laughs sadly) Classic Saturn. Listen... can I ask you something?",
        "Saturn: You’ve already asked with your silence. What’s troubling you?",
        "Jupiter: It’s Earth. She won’t talk to me. Or when she does, it’s cold... bitter.",
        "Saturn: Hmm... she’s been anxious lately. Waters rising, storms forming. She’s under pressure.",
        "Jupiter: I know that. But why push me away?",
        "Saturn: (sighs) She thinks you’re the reason behind it. The tides. The tsunamis.",
        "Jupiter: What?! That’s not me—well, not directly. I mean... gravity's complicated!",
        "Saturn: She doesn’t see the nuance. She sees her oceans swell and blames the biggest force nearby.",
        "Jupiter: But I’m the reason those asteroids don’t hit her! I *catch them*!",
        "Saturn: She doesn’t know, Jupiter. You’ve never told her.",
        "Jupiter: (softly) I didn’t want her to worry... I didn’t want her to fear the skies.",
        "Saturn: And so she fears *you* instead.",
        "Jupiter: (sits in silence) All this time... I’ve been the shield she thought was a threat.",
        "Jupiter: (stands tall) I have to tell her. She deserves to know.",
        "Narrator: Jupiter turns, heavier now — not from size, but from sorrow.",
        "Jupiter: (gently) Earth... can we talk? Please.",
        "Earth: (quietly) Why?",
        "Jupiter: Because something’s broken, and I want to fix it.",
        "Earth: (tense) You want to fix *me*? You’re the one pulling me apart!",
        "Jupiter: No. I want to fix *us*. You think I hurt you... I don’t.",
        "Earth: Then what *do* you do, Jupiter? Just sit there? Stir the tides?",
        "Jupiter: I watch the skies. I take the hits. I catch the comets meant for you.",
        "Earth: ...what?",
        "Jupiter: Do you remember Shoemaker-Levy 9? It could’ve changed your face forever. I took it in.",
        "Earth: That impact... I thought it was just a space event.",
        "Jupiter: It was. A deadly one. But it ended with me — not you.",
        "Earth: You’ve... been protecting me?",
        "Jupiter: Every day. Quietly. Without asking anything in return.",
        "Earth: Then why didn’t you say anything?",
        "Jupiter: Because I didn’t want you to see the dangers. I just wanted you to live.",
        "Earth: And I thought you were just heavy. Dangerous. Cold.",
        "Jupiter: I know I’m not easy to be around. I’m not gentle. I’m not small.",
        "Jupiter: But I’ve always looked out for you. Because you’re... everything.",
        "Earth: I’m sorry. I was scared. And when I’m scared, I push away.",
        "Jupiter: I get it. You’ve got a lot going on. Life. Oceans. Humanity. You're loud.",
        "Earth: (smiling) And you’re... big. And stubborn. And kind in a really quiet way.",
        "Jupiter: (softly) I’ll keep being your silent guardian. Whether you see me or not.",
        "Earth: No... I *want* to see you now.",
        "Jupiter: That means more than you know.",
        "Earth: So... friends again?",
        "Jupiter: Always.",
        "Narrator: And so, in the cold silence of space, a bond heals — vast, invisible, real.",
        "Saturn: (distantly, smiling) Maybe the universe doesn’t need gravity to pull hearts together.",
        "Jupiter: (softly) I’ll keep spinning. Watching. Protecting. That’s what I’m here for.",
        "Earth: (whispers) And I’ll never look at you the same again.",
        "Narrator: Earth believed Jupiter caused her chaos — the tides, the floods — not knowing tsunamis rise from within.",
        "Narrator: Tsunamis are the cries of shifting plates deep beneath her surface, not the whispers of distant gravity.",
        "Narrator: What she never saw were the asteroids, the frozen daggers of space, redirected by Jupiter’s pull.",
        "Narrator: Shoemaker-Levy 9 was one of many — a comet that Jupiter took into himself, without hesitation.",
        "Narrator: He bore the impact alone, quietly, so Earth could keep dancing — never knowing who saved her."
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("jupiter.html", story = story[0])


@app.route("/mercury", methods=["GET", "POST"])
def mercury_story():
    story = [
        "1",
        "2"
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("mercury.html", story = story[0])


if __name__ == "__main__":
    app.run(debug=True)
