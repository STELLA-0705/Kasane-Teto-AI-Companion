from rapidfuzz import fuzz


WAKE_WORDS = [
    "hey teto",
    "hey tito",
    "hey tato",
    "hey tenno",
    "hey teddo",
    "teto",
    "tito",
    "tato",
    "teddo"
]


def is_teto(text):

    text = text.lower()
    
    # remove punctuation
    text = "".join(
        c for c in text
        if c.isalnum() or c.isspace()
    )

    for wake in WAKE_WORDS:

        score = fuzz.ratio(text, wake)

        print(f"Wake check: {text} vs {wake} = {score}%")

        if score >= 65:
            return True

    return False