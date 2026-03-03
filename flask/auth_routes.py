"""
# TODO Jishnu
"""

from __future__ import annotations

from flask import Blueprint, request, jsonify, session

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Register a new user account.

    Request Body (JSON)
    -------------------
    username : str
        Desired display name. Must be unique.
    password : str
        Plain-text password (will be hashed server-side).

    Returns
    -------
    JSON
        ``{"message": "registered", "user_id": "<uuid>"}`` on success.
        ``{"error": "<reason>"}`` with HTTP 400/409 on failure.
    """
    # TODO Jishnu
    return jsonify({"error": "Not implemented"}), 501

@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Authenticate an existing user and start a session.

    Request Body (JSON)
    -------------------
    username : str
        Registered display name.
    password : str
        Plain-text password to verify.

    Returns
    -------
    JSON
        ``{"message": "logged in", "user_id": "<uuid>"}`` on success.
        ``{"error": "invalid credentials"}`` with HTTP 401 on failure.
    """
    # TODO Jishnu 
    return jsonify({"error": "Not implemented"}), 501

@auth_bp.route("/logout", methods=["POST"])
def logout():
    """
    End the current user's session.

    Returns
    -------
    JSON
        ``{"message": "logged out"}`` always.
    """
    # TODO Jishnu
    return jsonify({"error": "Not implemented"}), 501

@auth_bp.route("/me", methods=["GET"])
def me():
    """
    Return the currently authenticated user's public info.

    Returns
    -------
    JSON
        ``{"user_id": "<uuid>", "username": "<name>"}`` if logged in.
        ``{"error": "not authenticated"}`` with HTTP 401 otherwise.
    """
    # TODO Jishnu
    return jsonify({"error": "Not implemented"}), 501
