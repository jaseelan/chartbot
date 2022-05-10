import random

R_EATING = "Ohh don't like eating anything because I'm a bot obviously!"
R_ADVICE = "let me think about it, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
