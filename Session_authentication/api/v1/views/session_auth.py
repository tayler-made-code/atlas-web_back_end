#!/usr/bin/env python3

""" handles all routes for the Session authentication """

from flask import Flask, jsonify, request, abort, make_response
from models.user import User
from api.v1.auth.auth import Auth

app = Flask(__name__)


@app.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ longin route """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    user_search = User.search({'email': email})
    if not user_search:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_search[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    """ Create session ID for the User ID """
    session_id = auth.create_session(user.id)

    """ return dictionary representation of the User and set the cookie """
    user_json = user.to_json()
    response = make_response(user_json)
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
