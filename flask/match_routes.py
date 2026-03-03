"""
# TODO Kaarthik
"""

from __future__ import annotations

from flask import Blueprint, request, jsonify

match_bp = Blueprint("Match", __name__, url_prefix="/api/matches")    

@match_bp.route("/create", methods=["POST"])
def create_match():
    """
    Create a new match within a room.

    Request Body (JSON)
    -------------------
    room_id : str
        The room in which to create the match.
    host_type : str
        Either ``"COMPUTER"`` or ``"HUMAN"``.

    Returns
    -------
    JSON
        ``{"match_id": "<uuid>", "status": "WAITING"}`` on success.
    """
    # TODO Kaarthik
    return jsonify({"error": "Not implemented"}), 501

@match_bp.route("/<match_id>/start", methods=["POST"])
def start_match(match_id: str):
    """
    Start a match (transitions from WAITING to IN_PROGRESS).

    Parameters
    ----------
    match_id : str
        Path parameter.

    Returns
    -------
    JSON
        ``{"status": "IN_PROGRESS"}`` on success.
    """
    # TODO Kaarthik
    return jsonify({"error": "Not implemented"}), 501

@match_bp.route("/<match_id>/end", methods=["POST"])
def end_match(match_id: str):
    """
    Finalise a match.

    Parameters
    ----------
    match_id : str
        Path parameter.

    Returns
    -------
    JSON
        ``{"status": "COMPLETED", "result": {...}}`` on success.
    """
    # TODO Kaarthik
    return jsonify({"error": "Not implemented"}), 501

@match_bp.route("/<match_id>/state", methods=["GET"])
def get_match_state(match_id: str):
    """
    Return the live GameState of a match.

    Parameters
    ----------
    match_id : str
        Path parameter.

    Returns
    -------
    JSON
        Current round, phase, active players, and eliminated players.
    """
    # TODO Kaarthik
    return jsonify({"error": "Not implemented"}), 501

@match_bp.route("/<match_id>/rounds", methods=["GET"])
def get_rounds(match_id: str):
    """
    Return all rounds for a match.

    Parameters
    ----------
    match_id : str
        Path parameter.

    Returns
    -------
    JSON
        List of rounds with their turns.
    """
    # TODO Kaarthik
    return jsonify({"error": "Not implemented"}), 501

@match_bp.route("/<match_id>/rounds/<int:round_number>/turns", methods=["POST"])
def submit_turn(match_id: str, round_number: int):
    """
    Submit a player's turn response.

    Parameters
    ----------
    match_id : str
        Path parameter.
    round_number : int
        Path parameter — 1-based round index.

    Request Body (JSON)
    -------------------
    response : str
        The word or phrase the player says this round.

    Returns
    -------
    JSON
        ``{"locked": true}`` on success.
    """
    # TODO Kaarthik
    return jsonify({"error": "Not implemented"}), 501
