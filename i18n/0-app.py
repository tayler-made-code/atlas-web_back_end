#!/usr/bin/env python3

""" setup a basic Flask app in 0-app.py. Create a single / route and an
    index.html template that simply outputs “Welcome to Holberton” as
    page title (<title>) and “Hello world” as header (<h1>) """

from flask import Flask, render_template

app = Flask(__name__)

""" Create a single / route and an index.html template that simply outputs """
@app.route('/')
def hello_world():
    """ outputs “Welcome to Holberton” as page title (<title>)
      and “Hello world" as header (<h1>) """
    title = "Welcome to Holberton"
    header = "Hello world"
    return render_template('0-index.html', title=title, header=header)
