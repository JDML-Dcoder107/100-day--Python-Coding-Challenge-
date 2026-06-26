#Project Quiz Game
import random

questions = {
    "What is the capital of the Philippines?": "Manila",
    "What is the language that Guido van Rossum created?": "Python",
    "What is the hotest planet in the solar system?": "Venus",
    "What is the hardest loving someone you can't have or someone you can't love?": "Wala kasi di pa ako minamahal ngayon",
    "What is the most abundant gas in the Earth's atmosphere?": "Nitrogen",
    "What does the acronym 'API' stand for?": "Application Programming Interface",
    "What is the layer 3 of the OSI model?": "Network Layer"
}

print(" Welcome to the Quiz Game! ".center(50, "="))

question = random.choice(list(questions.keys()))
answer = input(f"{question}: ")
if answer.title() == questions[question]:
    print("Correct!")
else:
    print(f"Incorrect! The correct answer is {questions[question]}")
