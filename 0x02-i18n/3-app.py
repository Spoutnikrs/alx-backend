#!/usr/bin/env python3
""" A script for basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)
app.jinja_env.autoescape = True

class Config:
    """A class for configuration settings for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'

app.config.from_object(Config)

def get_locale():
    """This function determines the best match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def hello():
    """A function that renders a template file"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)