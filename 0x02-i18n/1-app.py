#!/usr/bin/env python3
""" A script for basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """A class that configures the app settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


@app.route("/")
def hello():
    """ A function that renders a basic template"""
    return render_template('1-0-index.html')


if __name__ == '__main__':
    app.run()
