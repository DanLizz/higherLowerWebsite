from flask import Flask
import random

app = Flask(__name__)


# Generate random number between 1 to 9
def generate_number():
    guess_number = random.randint(1, 9)
    return guess_number

generated_number = generate_number()


@app.route('/')
def hello_world():
    return '<body style="text-align:center"><h1>Hello!</h1><p>Guess a number between 1 to ' \
           '9</p><img ' \
           'src="https://media1.giphy.com/media/SScTyz7dQ0Gf7c9dZ9/giphy.gif?cid' \
           '=ecf05e47y6ob5gygf8bu5b9rilxjt2k0jcw7t3afndwitayo&rid=giphy.gif&ct=g"></body>'


@app.route('/<int:number>')
def check_number(number):
    if generated_number == number:
        return f'<body style="text-align:center"><h1> You guessed it right!</h1><img ' \
               f'src="https://media2.giphy.com/media/RJzv5gG13bFsER317k/giphy.gif' \
               '?cid=ecf05e47y6ob5gygf8bu5b9rilxjt2k0jcw7t3afndwitayo&rid=giphy.gif&ct=g' \
               '-RJzv5gG13bFsER317k"></body> '
    elif generated_number > number:
        return f'<body style="text-align:center"><h1> Your guess is too low!</h1><img ' \
               f'src="https://media3.giphy.com/media/QXIkWVGOjIpuutoo7y/giphy' \
               '.gif?cid=ecf05e47y6ob5gygf8bu5b9rilxjt2k0jcw7t3afndwitayo&rid=giphy.gif&ct=g"></body> '
    else:
        return f'<body style="text-align:center"><h1> Your guess is too high!</h1><img ' \
               f'src="https://media3.giphy.com/media/efarUnu8xCMXm6BUj2/giphy' \
               '.gif?cid=ecf05e475kupc7undlqott8jlu3yohhipzu4984g780a737m&rid=giphy.gif&ct=g"></body> '


if __name__ == "__main__":
    app.run(debug=True)
