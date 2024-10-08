from flask import Flask
from greetlib.greet import Greet
app = Flask(__name__)


@app.route("/")
def index():
    message = "{} World!".format(Greet.forLocale("en"))
    return message


if __name__ == "__main__":
    app.run(host='0.0.0.0')
