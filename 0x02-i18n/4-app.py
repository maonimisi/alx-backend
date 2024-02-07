#!/usr/bin/env python3
"""
  Setup a basic Flask app in 0-app.py. Create a single / route and an
  index.html template that simply outputs “Welcome to Holberton” as page
  title (<title>) and “Hello world” as header (<h1>).
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from os import getenv


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route("/", strict_slashes=False)
def index() -> str:
    "This rounte render 1-index.html from the templates directory"
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """Function, detect if the incoming request contains locale argument
    and ifs value is a supported locale"""
    if request.args.get('locale'):
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)