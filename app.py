#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/hello")
def hai():
    return "Oh hai, World!"


if __name__ == "__main__":
    app.run(debug=True)
