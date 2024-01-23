#!/usr/bin/env python3

""" Session Auth """

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ user id by session id class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create session """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user id for session id """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ current user """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        from models.user import User
        return User.get(user_id)
