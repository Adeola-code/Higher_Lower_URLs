import random
from flask import Flask

app = Flask(__name__)

random_number = random.randint(0,10)

@app.route("/")
def index():
    return ("<h1 style='text-align:center'>Guess a number between 0 and 9 and type in URL<h1/><img  "
            "src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' style='padding-left:630px'>")


@app.route("/<int:number>")
def guess(number):
    if number == random_number:
        return ("<h1 style='text-align:center'>And that is Correct!!<h1/><img  "
                "src='https://media.giphy.com/media/ffpwvIeYLNzDKdtCYw/giphy.gif' style='padding-left:550px'>")
    elif number < random_number:
        return "<h1 style='text-align:center'>Too low!<h1/><img  src='https://media.giphy.com/media/MUmKWzDCU8Z3MVxjls/giphy.gif' style='padding-left:550px'>"
    else:
        return "<h1 style='text-align:center'>That's too high<h1/><img  src='https://media.giphy.com/media/3o6Zt8XfhAdl4QPZ4I/giphy.gif' style='padding-left:550px'>"


if __name__ == "__main__":
    app.run(debug=True)