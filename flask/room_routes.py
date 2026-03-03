"""
# TODO Sharvesh
"""

from __future__ import annotations

from flask import Blueprint, request, jsonify, session

room_bp = Blueprint("Room", __name__, url_prefix="/api/rooms")


@room_bp.route("/create", methods=["POST"])
def create_room():
    """
    Create a new game room.

    Request Body (JSON)
    -------------------
    (no body required — room_id and access_code are generated server-side)

    Returns
    -------
    JSON
        ``{"room_id": "<uuid>", "access_code": "<code>"}`` on success.
    """
    # TODO Sharvesh
    return jsonify({"error": "Not implemented"}), 501

@room_bp.route("/join", methods=["POST"])
def join_room():
    """
    Join an existing room using its access code.

    Request Body (JSON)
    -------------------
    access_code : str
        The short code for the room to join.

    Returns
    -------
    JSON
        ``{"room_id": "<uuid>", "message": "joined"}`` on success.
        ``{"error": "room not found"}`` with HTTP 404 if invalid.
    """
    # TODO Sharvesh
    return jsonify({"error": "Not implemented"}), 501

@room_bp.route("/<room_id>/leave", methods=["POST"])
def leave_room(room_id: str):
    """
    Remove the current user from a room.

    Parameters
    ----------
    room_id : str
        Path parameter — the room to leave.

    Returns
    -------
    JSON
        ``{"message": "left room"}`` on success.
    """
    # TODO Sharvesh
    return jsonify({"error": "Not implemented"}), 501

@room_bp.route("/<room_id>", methods=["GET"])
def get_room(room_id: str):
    """
    Return details about a specific room.

    Parameters
    ----------
    room_id : str
        Path parameter — the room to query.

    Returns
    -------
    JSON
        Room details including member list and match history summary.
    """
    # TODO Sharvesh
    return jsonify({"error": "Not implemented"}), 501


# ---------------------------------------------------------------------------
# GET /api/rooms/<room_id>/leaderboard
# ---------------------------------------------------------------------------

@room_bp.route("/<room_id>/leaderboard", methods=["GET"])
def get_leaderboard(room_id: str):
    """
    Return the current leaderboard for a room.

    Parameters
    ----------
    room_id : str
        Path parameter — the room whose leaderboard to fetch.

    Returns
    -------
    JSON
        ``{"rankings": [{"user_id": "...", "score": ..., "rank": ...}]}``
    """
    # TODO
    return jsonify({"error": "Not implemented"}), 501
