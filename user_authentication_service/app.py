#!/usr/bin/env python3

""" Basic Flask app """

from flask import Flask, jsonify, request, make_response, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home() -> str:
    response = {
        'message': 'Bienvenue'
    }
    return jsonify(response), 200


@app.route('/users', methods=['POST'])
def register_user():
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
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.login_user(email, password)
        if not user:
            abort(401)
        else:
            session_id = AUTH.create_session(user.id)
            response = make_response(jsonify({
                'email': user.email,
                'message': 'logged in'
            }))
            response.set_cookie('session_id', session_id)
            return response
    except ValueError:
        return jsonify({
            'message': 'Invalid login credentials'
        }), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
