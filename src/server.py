from flask import *
from random import randint

START_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

app = Flask(__name__)


@app.route("/")
def header():
    return '<h1>Guess a number between 0 and 9</h1>' \
           f'\n<img src="{START_GIF}"/>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        text = "Too high, try again!"
        color = "blue"
        gif_link = HIGH
    elif guess < number:
        text = "Too low, try again!"
        color = "red"
        gif_link = LOW
    else:
        text = "You got me!"
        color = "green"
        gif_link = CORRECT
    return f'<h1 style="color: {color}">{text}</h1>' \
           f'\n<img src="{gif_link}"/>'


if __name__ == "__main__":
    number = randint(0, 9)
    print(number)
    app.run(debug=True)
