#!/usr/bin/env python3
""" A script for basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """A class for configuration settings for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """This function determines the best match for the supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello():
    """A function that returns a rendered template for the route /"""
    return render_template('1-0-index.html')


if __name__ == '__main__':
    app.run()
