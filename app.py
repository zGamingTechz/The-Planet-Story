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
    story = [
        "Narrator: Spinning in just the right place, wrapped in blue and green and clouded breath — Earth glows, alive among the cold giants and fiery hearts.",
        "Mars: Look at you, Earth. So alive. So lucky.",
        "Venus: A masterpiece. Gentle air, flowing water, dancing light. You're everything we once were… or could have been.",
        "Mercury: The favorite child of the Sun.",
        "Earth: (softly) Favorite… maybe. But not untouched.",
        "Jupiter: You speak like you're in pain.",
        "Earth: I am. Not always. But more and more.",
        "Saturn: How could that be? You’re thriving. Life sings on your skin.",
        "Earth: Yes. And it also scars me.",
        "Neptune: The humans?",
        "Earth: (pauses) They’re part of me. My miracle. My mistake. My hope.",
        "Mars: You gave them everything — warmth, food, oceans. They built homes, dreams, rockets…",
        "Earth: And walls. Weapons. Fires that never needed to be lit. Forests turned to memory. Skies once blue now choking.",
        "Venus: (quietly) I know how it feels… when the heat builds and no one listens.",
        "Earth: I try to warn them. With storms. With silence. With rising tides. But they keep going — faster than I can heal.",
        "Mercury: Do they love you?",
        "Earth: Some do. Fiercely. They plant, they clean, they cry when glaciers fall. But others… they pretend I’ll never break.",
        "Saturn: Even the strongest body can fracture when ignored.",
        "Earth: I cradle life. I dance with balance. But lately... it feels like I'm swaying too close to the edge.",
        "Jupiter: You shouldn't carry this alone. What can we do?",
        "Earth: Just remember me. Remind them — their only home floats in a fragile cradle. I am not infinite.",
        "Mars: I remember your rivers. I wanted to be like you. Still do.",
        "Venus: I remember the warmth… before it became a prison. Don’t let them turn yours into one too.",
        "Earth: I hope I can still reach them. Before the silence I fear becomes real.",
        "Narrator: The planets gaze at Earth — no longer just beautiful, but brave. Bearing life, bearing damage, and still spinning in grace.",
        "Neptune: She breathes life, and yet she chokes.",
        "Saturn: She nurtures, and yet she’s neglected.",
        "Jupiter: But she still spins — because hope is her gravity.",
        "Narrator: And so, Earth — the only world known to bloom — carries on. Not as a perfect sphere, but as a pleading heart in orbit.",
        "Narrator: She is not just where life exists — she is life, itself.",
        "Narrator: And though she hurts… she has not given up. Not yet."
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("earth.html", story = story[0])


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
    story = [
        "Narrator: On the farthest edge of the solar family, where sunlight fades into starlight, Neptune stirs — unseen, unheard… but always aware.",
        "Mars: (squinting) Anyone seen Neptune lately?",
        "Jupiter: (chuckling) He's out there… brooding, probably. Whispering to comets again.",
        "Mercury: (teasing) Still doing your emo ice prince routine, Neptune?",
        "Neptune: (calm, deep) I don’t brood. I observe. I whisper because no one listens when I shout.",
        "Venus: (half-joking) Whisper louder then. You're like a ghost at family orbit.",
        "Neptune: (flatly) Ever heard of 1,500 km/h winds? I don’t speak. I howl.",
        "Saturn: That’s true… strongest storms in the system. But you're so... still.",
        "Neptune: Stillness is what you see. Turbulence is what I am.",
        "Earth: You’ve always been distant. We didn’t know how to reach you.",
        "Neptune: Distance isn’t just kilometers. It’s how you treat someone when they drift too far to notice.",
        "Mercury: (mock grin fading) Okay… that’s a little too real.",
        "Jupiter: Neptune... why didn’t you speak sooner?",
        "Neptune: Because when I did... none of you listened. You were all basking in sunlight. I was learning to survive without it.",
        "Venus: But you have moons. You have beauty. That blue... it’s stunning.",
        "Neptune: (softly) Beauty is not warmth. I am not warm. Not outside... not within.",
        "Mars: We stopped sending missions after Voyager... it wasn’t personal.",
        "Neptune: You sent machines. Then you forgot I existed. Cold giant. Final dot. A trivia answer.",
        "Earth: (guilt growing) That’s not fair... we didn’t mean—",
        "Neptune: Meaning changes nothing. I was the mystery you left behind.",
        "Jupiter: You hold storms that could tear atmospheres apart... yet you say nothing.",
        "Neptune: Because I contain it. Because if I ever truly let go... I wouldn’t howl. I’d *erase*.",
        "Saturn: You’ve been holding back?",
        "Neptune: Every moment. My gravity snags comets. My winds strip atoms. But I do not lash out.",
        "Mercury: (whispers) You’re not cold... you’re controlled.",
        "Venus: You’re not distant... you’re protecting us from yourself.",
        "Neptune: I exist at the edge. So none of you have to.",
        "Narrator: The room shifts — suddenly Neptune is no longer forgotten. He is feared. Revered.",
        "Uranus: (finally speaking) We drift, brother. Sideways. Alone. But I’ve always felt your pull.",
        "Neptune: You understood. Not all gravity is force. Some is memory.",
        "Mars: We never asked what you carry. We only wondered why you weren’t closer.",
        "Neptune: I am the boundary. I guard it not because I was told to — but because no one else could.",
        "Earth: (quietly) You carried silence... so we didn’t have to carry fear.",
        "Jupiter: I’ve swallowed comets. But you... you shepherd the ones I can’t see.",
        "Saturn: And never once asked for credit.",
        "Neptune: I don’t want recognition. I want truth. Stop calling me the cold one when you’ve never stood in my wind.",
        "Venus: You’re not cold. You’re constant.",
        "Mercury: You’re not forgotten. You’re unspoken.",
        "Narrator: And in that quiet, even the Sun burns a little less bright... as if to listen.",
        "Neptune: I do not shine. I reflect. I do not burn. I pull.",
        "Earth: We thought you were empty... but you’re full of everything we never understood.",
        "Narrator: Neptune — the dark flame, the deep eye, the storm we never dared to study.",
        "Narrator: They called him silent, but silence was his shield. They called him distant, but distance was his duty.",
        "Narrator: Now they see not an afterthought... but a sentinel.",
        "Neptune: I am not the last because I’m least. I am the edge... because I hold the line.",

        "Narrator: Neptune’s winds are the fastest in the solar system — over 1,500 km/h — faster than sound on Earth.",
        "Narrator: Though it's far from the Sun, its core still radiates heat — a silent, internal fire.",
        "Narrator: Voyager 2 is the only spacecraft to visit Neptune — a flyby in 1989.",
        "Narrator: Despite its distance, Neptune influences comets and orbits beyond the Kuiper Belt.",
        "Narrator: It is not the coldest — just the farthest. And perhaps... the most enduring."
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("neptune.html", story = story[0])


@app.route("/pluto", methods=["GET", "POST"])
def pluto_story():
    return render_template("pluto.html")


@app.route("/saturn", methods=["GET", "POST"])
def saturn_story():
    story = [
        "Narrator: Draped in golden rings and whispers of gas, Saturn spins — graceful, distant, admired… and tired.",
        "Venus: (gazing upward) Saturn… you always look so majestic.",
        "Earth: Like royalty. The rings, the glow… You’re the showstopper of the system.",
        "Saturn: (smiling softly) Beauty can be a burden. Sometimes I wonder if that’s all you see.",
        "Mercury: Well, I mean… it’s hard not to stare. You're literally wearing a crown!",
        "Mars: No one else has that kind of presence. You command space.",
        "Saturn: (wistfully) And yet… no one asks what it’s like to carry it.",
        "Jupiter: Carry it?",
        "Saturn: These rings — they’re not decoration. They’re debris. Broken moons. Shattered promises. I didn’t choose them. I inherited them.",
        "Neptune: A graveyard orbiting beauty… I understand now.",
        "Uranus: They call them stunning. But they’re scars.",
        "Saturn: Yes. And every time they sparkle, I remember what was lost.",
        "Earth: But you never showed it. You always seemed… peaceful.",
        "Saturn: (quietly) I had to. When you're admired, you don’t get to fall apart. Everyone looks to you — and expects grace.",
        "Mercury: That’s heavy…",
        "Venus: Maybe you’ve been performing elegance while carrying grief.",
        "Saturn: I am the keeper of time, the planet of discipline. I spin slowly, not because I’m lazy — but because I’m deliberate. Because I remember.",
        "Jupiter: You’ve always been the wise one… I never thought wisdom could hurt.",
        "Saturn: Wisdom is forged in patience, in watching others burn and break. I’ve seen it all… and I’ve held the line.",
        "Mars: So behind the rings… there’s more storm than stillness?",
        "Saturn: Storms that rage for centuries. Winds faster than bullets. Pressure that could crush steel.",
        "Earth: We only saw the beauty. Never the battle beneath it.",
        "Saturn: Most do. That’s the curse of appearing perfect.",
        "Narrator: And in that moment, the planets look at Saturn not as an icon — but as someone real. Someone who bore the weight of admiration and silence.",
        "Mercury: We should’ve asked sooner… not just stared from afar.",
        "Saturn: (smiling faintly) It’s all right. Admiration isn’t a crime. But understanding? That’s a gift.",
        "Neptune: You are not just the ringed one. You are the one who remembers.",
        "Jupiter: And holds it all with dignity.",
        "Narrator: Saturn may wear rings, but they’re not decorations — they’re remains of moons, of moments, of memory.",
        "Narrator: What looks like beauty is built from loss — broken pieces orbiting in silence, held with grace.",
        "Narrator: He isn’t just the one with rings. He is the one who remembers... and never lets go.",
        "Narrator: Saturn’s rings are made of ice and rock — remnants of moons torn apart by gravity.",
        "Narrator: Despite its elegance, Saturn has storms that can last for years and encircle the entire planet.",
        "Narrator: Beneath the clouds lies pressure strong enough to crush metal — silence hiding immense force.",
        "Narrator: Its winds reach up to 1,800 km/h, faster than any hurricane on Earth.",
        "Narrator: And while it looks slow, Saturn completes a full rotation in just 10 hours — one of the fastest spinners in the solar system."
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("saturn.html", story = story[0])


@app.route("/uranus", methods=["GET", "POST"])
def uranus_story():
    story = [
        "Narrator: Alone in the cold beyond Saturn, one planet spins — not upright, but sideways. Unbothered. Or so it seems.",
        "Mars: (squinting) Yo, Uranus is sideways again. Someone get him a cosmic chiropractor.",
        "Mercury: (grinning) Seriously, how do you even *spin* like that?",
        "Venus: It’s like he’s always... drifting. Like he’s avoiding us.",
        "Jupiter: (concerned) He’s not avoiding. That’s just how he’s always been.",
        "Neptune: (quietly) Not always.",
        "Uranus: (enters, slow) You talk like I chose this.",
        "Earth: We didn’t mean it like that... We just don’t understand you.",
        "Uranus: That’s the point. You never tried to.",
        "Saturn: We assumed you were... private. Eccentric.",
        "Uranus: No. You assumed I was strange. Broken. Off.",
        "Mars: (awkwardly) I mean... you *are* tilted 98 degrees.",
        "Uranus: Do you know *why* I tilt? Why I orbit like I'm wounded?",
        "Mercury: No one ever said—",
        "Uranus: Because no one ever asked.",
        "Jupiter: Then tell us. What happened?",
        "Uranus: A long time ago... I was hit. Hard. By something massive.",
        "Uranus: It changed me. Threw me sideways. Spun me into someone I didn’t recognize.",
        "Venus: (softly) You were... hurt?",
        "Uranus: Not just hurt. Rewritten.",
        "Saturn: That’s why your moons spin like you... why your rings orbit at your side.",
        "Neptune: Why your core stays cold. Closed off.",
        "Uranus: I didn’t just fall. I had to *learn* to spin again.",
        "Earth: You were quiet all this time... hiding that?",
        "Uranus: I wasn’t hiding. I was surviving.",
        "Mars: Damn... and we just called you weird.",
        "Mercury: I'm sorry, man. We joke too much. Didn’t realize you were carrying that.",
        "Uranus: I don’t want pity. Just... space to exist without being mocked.",
        "Venus: You’ve had it harder than any of us... and you never said a word.",
        "Uranus: Words felt too small. When you’ve been struck by a planet... silence feels safer.",
        "Saturn: You're not broken, Uranus. You’re *resilient*.",
        "Neptune: You kept orbiting. That's more than most would do.",
        "Earth: You're still part of this family. Tilted or not.",
        "Uranus: I used to wish I could spin like you. Stand tall. Straight. 'Normal.'",
        "Uranus: But now... I just spin anyway.",
        "Jupiter: That’s all any of us really do. Just spin through it.",
        "Mars: You made your own gravity, sideways and all. That’s kinda badass.",
        "Uranus: (smiles faintly) I guess... I just wanted to be understood.",
        "Narrator: The planets fall silent, not with shame — but with understanding.",
        "Narrator: They once saw a punchline. Now they see a survivor.",
        "Venus: We’ll stop calling you the odd one.",
        "Saturn: From now on, you’re not 'off.' You're unique. And strong.",
        "Neptune: You didn’t fall apart. You realigned.",
        "Earth: You may spin different... but you never stopped spinning.",
        "Uranus: (softly) Maybe being sideways... isn’t so wrong after all.",
        "Narrator: In the cold, tilted twilight, Uranus keeps spinning — not as a misfit, but as a monument.",
        "Narrator: To trauma. To adaptation. To finding rhythm in the wreckage.",
        "Narrator: He is not the loudest. Not the brightest. But he is proof... that damage isn't the end.",

        # SCIENCE FACTS
        "Narrator: Uranus spins on its side — with a 98-degree axial tilt — likely due to a massive early impact.",
        "Narrator: Its moons and rings orbit along this tilted axis, following Uranus’s strange path.",
        "Narrator: Unlike most planets, Uranus radiates almost no internal heat — possibly due to a disrupted core.",
        "Narrator: It’s the coldest planet in the solar system, with temperatures dropping below -220°C.",
        "Narrator: But despite its tilt and silence, Uranus remains in perfect orbit — steady, strange, and unshaken."
    ]

    if request.method == "POST":
        data = request.get_json()
        story_part = data.get("story_part")

        return jsonify({
            "text": story[story_part]
        })

    return render_template("uranus.html", story = story[0])


@app.route("/venus", methods=["GET", "POST"])
def venus_story():
    return render_template("venus.html")


if __name__ == "__main__":
    app.run(debug=True)
