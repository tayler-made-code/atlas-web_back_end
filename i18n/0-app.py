#!/usr/bin/env python3

""" basic Flask app in 0-app.py """

from flask import Flask, render_template

app = Flask(__name__)

""" Create a single / route and an index.html template that simply outputs """
@app.route('/')
def hello_world():
    """ render a template """
    return render_template('0-index.html')
