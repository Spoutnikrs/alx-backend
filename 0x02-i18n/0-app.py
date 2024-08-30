#!/usr/bin/env python3
""" A script for basic flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    """ A function that renders a basic template """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
