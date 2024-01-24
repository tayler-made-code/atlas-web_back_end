#!/usr/bin/env python3

""" Basic Flask app """

from flask import Flask, jsonify, request, make_response, abort
from flask import redirect, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home() -> str:
    """ Method that returns a message for the / route """
    response = {
        'message': 'Bienvenue'
    }
    return jsonify(response), 200


@app.route('/users', methods=['POST'])
def register_user():
    """ Method that registers a new user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({
            'email': new_user.email,
            'message': 'user created'
        })
    except ValueError:
        return jsonify({
            'message': 'email already registered'
        }), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ Method that checks if the email and password matches a user """
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(jsonify({
            'email': email,
            'message': 'logged in'
        }), 200)
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Method that deletes the user session / logout """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for('home')), 302
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """ Method that finds the user corresponding to the session ID """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({
            'email': user.email
        }), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def reset_password():
    """ Method that generates a token """
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({
            'email': email,
            'reset_token': reset_token
        }), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def new_password():
    """ Method that updates the password """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    password = request.form.get('hashed_password')
    try:
        AUTH.update_password(reset_token, password)
        return jsonify({
            'email': email,
            'message': 'Password updated'
        }), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
