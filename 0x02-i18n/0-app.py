#!/usr/bin/env python3
"""
  Setup a basic Flask app in 0-app.py. Create a single / route and an
  index.html template that simply outputs “Welcome to Holberton” as page
  title (<title>) and “Hello world” as header (<h1>).
"""
from flask import Flask, render_template
from os import getenv


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index() -> str:
    "This rounte render 0-index.html from the templates directory"
    return render_template('0-index.html')


if __name__ == '__main__':
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
