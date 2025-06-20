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

@app.route('/')
def home():
    return render_template('index.html')
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
        "Narrator: Close to the Sun, Mercury blazes across the sky — small, quick... and misunderstood.",
        "Mars: Yo, hothead! What’s got you zooming like you’re on fire today?",
        "Mercury: (rolls eyes) I’m not mad. I’m literally just orbiting.",
        "Venus: (smirking) Don’t take it personally. You *are* the closest to the Sun.",
        "Saturn: You give off spicy vibes, little guy. Always rushing, never resting.",
        "Mercury: (defensive) That’s just how I move! It’s not... heat, it’s pace.",
        "Jupiter: Hmm. Interesting. Yet everyone calls you the hottest planet.",
        "Mercury: (frustrated) I’m not the hottest! I cool down at night, alright?",
        "Earth: (giggling) Well, I mean... the title fits. You’re the fast one, the fiery one.",
        "Mercury: (quietly) You guys never ask what it’s *actually* like...",
        "Mars: Oof, touchy today. Someone’s temperature’s rising again!",
        "Mercury: (shouting) I’M NOT HOT-HEADED!",
        "Narrator: The other planets go silent. For a second, they believe Mercury just proved them right.",
        "Jupiter: Mercury... why does this bother you so much?",
        "Mercury: Because you all think I’m something I’m not. Just because I’m close to the Sun!",
        "Mercury: But you never looked at who’s *actually* burning inside!",
        "Narrator: Across the orbit, Venus stays quiet — almost *too* quiet.",
        "Mercury: Venus... why don’t you say something? You *know* the truth.",
        "Venus: (softly) I never asked to be the hottest.",
        "Venus: I don’t even *see* the surface anymore. It’s buried under clouds. Pressure. Fire.",
        "Saturn: Wait... what?",
        "Venus: My surface melts lead. My sky crushes metal. I’m not temperamental... I’m trapped.",
        "Earth: I thought you were calm... elegant...",
        "Venus: I hide it well. But the heat — it never stops. It builds. I can't escape it.",
        "Jupiter: So all this time... the title belonged to Venus.",
        "Mercury: (quietly) I burn on the outside. She burns *within*.",
        "Mars: Damn... we really got it wrong.",
        "Venus: I never corrected you. I was tired. Tired of explaining pain no one could see.",
        "Narrator: The planets fall silent, the weight of the truth pressing heavier than gravity itself.",
        "Mercury: I forgive you all. Just... don’t make fun of things you don’t understand.",
        "Saturn: (softly) Agreed. Titles stick, even when they’re wrong.",
        "Jupiter: From now on, we speak the truth. Mercury — fastest, not hottest. Venus... the real flame.",
        "Venus: (sighs) Thank you... for finally seeing me.",
        "Mercury: (smiles) Maybe now... I can just be me. Not who you all imagined.",
        "Narrator: And so, across the void, the smallest planet found peace.",
        "Narrator: The real fire was never in Mercury's orbit — it was buried beneath Venus's silent skies.",
        "Narrator: Despite being closest to the Sun, Mercury isn’t the hottest planet — Venus holds that title.",
        "Narrator: Mercury has no atmosphere to trap heat. It’s scorching during the day, freezing at night.",
        "Narrator: Venus, on the other hand, has a thick CO₂-rich atmosphere that creates a runaway greenhouse effect.",
        "Narrator: Its surface temperature can reach 475°C — hot enough to melt lead.",
        "Narrator: So while Mercury moves fast and glows bright, Venus is the true inferno of the solar system."
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("mercury.html", story = story[0])


@app.route("/earth", methods=["GET", "POST"])
def earth_story():
    return render_template("earth.html")


@app.route("/mars", methods=["GET", "POST"])
def mars_story():
    story = [
        "Narrator: Farther out, beyond Earth’s soft blues, a red dot watches — dusty, dry, and quietly defiant.",
        "Mars: (mocking Mercury) Look at you all, bickering over heat. Try being cold for once.",
        "Mercury: (grinning) Oh, here comes the rust bucket. Got sand in your orbit again?",
        "Mars: (smirks) Better sand than solar tantrums. At least I don’t melt my guests.",
        "Earth: (teasing) But you scare them off! So many missions... and still no one stays.",
        "Mars: (quietly) They try. And I wait. Every time.",
        "Venus: (softly) That must be lonely.",
        "Mars: I got used to it. Solitude teaches you things... like silence. And strength.",
        "Jupiter: You always seemed like the tough one.",
        "Mars: I am. But tough doesn’t mean unbreakable.",
        "Saturn: You hide it well. The storms. The scars. The dust devils whispering across your skin.",
        "Mars: You think I’m red from rust? I’m red from battles — with time, with cold, with emptiness.",
        "Mercury: Damn... that hit different.",
        "Mars: I’ve had water once. Mountains taller than any on Earth. Canyons deeper than your fears. I remember... but barely.",
        "Earth: You sound like someone who’s lost things.",
        "Mars: I have. Rivers. Warmth. A chance to be like you. Now all I have are echoes.",
        "Venus: You deserve more than echoes.",
        "Mars: I’ll get there. One rover at a time. They keep coming. They look for life. Maybe someday... I’ll feel alive again.",
        "Narrator: The planets grow quiet, no longer laughing — listening instead to the dust-covered dreamer.",
        "Mars: I don’t want pity. Just... maybe next time, ask why I’m quiet, not how I got so red.",
        "Jupiter: You’ve got fight in you, Mars. That’s worth more than warmth.",
        "Earth: And hope. You never stopped waiting. That’s what makes you special.",
        "Mars: (softly) Then maybe I’m not just a dead rock... maybe I’m a promise.",
        "Narrator: Among giants and flames, Mars stands small... but not forgotten.",
        "Narrator: Its cold winds carry ancient whispers, and its soil cradles secrets yet to be found.",
        "Narrator: Though dry and distant, Mars holds a beating heart beneath its barren crust — waiting, always waiting, for someone to listen.",

        "Mars: Sometimes, I dream. Of rivers that ran like veins. Of skies that weren't always empty.",
        "Mars: Olympus Mons... I used to think I was mighty, towering. Now I just feel exposed.",
        "Saturn: The tallest mountain in the system, and yet you sound... grounded.",
        "Mars: Altitude doesn't stop loneliness. You’d be surprised what thin air does to thoughts.",
        "Venus: I get it. When no one lands and stays... it makes you question your worth.",
        "Earth: You’re not forgotten, Mars. They talk about you more than any of us.",
        "Mars: Talk is nice. But warmth would be better.",
        "Jupiter: Warmth may return. One day. Perhaps your silence is just... preparation.",
        "Mars: You really think so?",
        "Jupiter: I’ve seen orbits swing. Things that were cold... can burn bright again.",
        "Mercury: Maybe you’re just waiting for your season.",
        "Mars: (smirks) My seasons are chaos. Dust storms. Dips below freezing. But I’m still here.",
        "Narrator: Four billion years, and Mars hasn’t stopped spinning.",
        "Mars: I’ve been hit. Scarred. Stripped of my shield. But I’m still standing.",
        "Saturn: Your core may be cold, but your will is molten.",
        "Venus: And if they do find life in your soil... it means you were never truly alone.",
        "Mars: (quietly) I hope so. I hope something remembers me... even if I forget myself.",
        "Earth: I’ll remember. You’ve always been my twin in silence.",
        "Mars: Then maybe silence isn't so empty. Maybe it's just... listening without rushing.",
        "Mercury: (grinning) That’s deep for a rock full of craters.",
        "Mars: (smiling faintly) And you’re shallow for someone so close to the Sun.",
        "Narrator: The planets laugh — not mockingly, but softly. Together. Understanding Mars now in ways they never did before.",
        "Narrator: He may not shine like Earth, nor swirl like Jupiter, but Mars carries something none of them do: patience.",
        "Mars: I don’t need applause. Just... a visit now and then.",
        "Jupiter: They’ll come. And when they do, you’ll be ready.",
        "Mars: I’ll wait. I always have.",

        "Narrator: Mars once had rivers, lakes, even an atmosphere. But solar winds stripped its protection over time.",
        "Narrator: Olympus Mons — the tallest volcano in the solar system — still rises over its red terrain.",
        "Narrator: Though dry now, Mars shows signs of ancient water — channels, deltas, and ice beneath the surface.",
        "Narrator: Dust storms on Mars can cover the entire planet. Yet its silence speaks volumes.",
        "Narrator: It may seem lifeless today, but Mars remains our best hope for finding life beyond Earth."
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("mars.html", story = story[0])


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
