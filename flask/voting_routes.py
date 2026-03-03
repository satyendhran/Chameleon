"""
# TODO Ambika
"""

from __future__ import annotations

from flask import Blueprint, request, jsonify

voting_bp = Blueprint("voting", __name__, url_prefix="/api/vote")

@voting_bp.route("/mode", methods=["POST"])
def vote_mode():
    """
    Submit a vote for the game mode selection phase.

    Request Body (JSON)
    -------------------
    match_id : str
        The match currently in lobby/pre-game.
    choice : str
        The mode name the player is voting for.

    Returns
    -------
    JSON
        ``{"message": "vote recorded"}`` or ``{"winner": "<mode>"}`` if voting complete.
    """
    # TODO Ambika
    return jsonify({"error": "Not implemented"}), 501

@voting_bp.route("/eliminate", methods=["POST"])
def vote_eliminate():
    """
    Submit an elimination vote during a round's voting phase.

    Request Body (JSON)
    -------------------
    match_id : str
        Active match ID.
    target_player_id : str
        The player being voted against.

    Returns
    -------
    JSON
        ``{"message": "vote recorded"}`` or ``{"eliminated": "<player_id>"}`` if voting complete.
    """
    # TODO Ambika
    return jsonify({"error": "Not implemented"}), 501

@voting_bp.route("/award", methods=["POST"])
def vote_award():
    """
    Submit an award vote at the end of a match.

    Request Body (JSON)
    -------------------
    match_id : str
        Completed match ID.
    award_type : str
        One of ``"GOATED"``, ``"GENERALIST"``, ``"AARONIC"``.
    nominee_id : str
        The player being nominated for this award.

    Returns
    -------
    JSON
        ``{"message": "vote recorded"}`` or ``{"awards": {...}}`` if all award votes complete.
    """
    # TODO Ambika
    return jsonify({"error": "Not implemented"}), 501

@voting_bp.route("/<match_id>/results", methods=["GET"])
def get_vote_results(match_id: str):
    """
    Return the latest vote tallies and results for a match.

    Parameters
    ----------
    match_id : str
        Path parameter.

    Returns
    -------
    JSON
        Current vote counts for the active vote phase.
    """
    # TODO Ambika
    return jsonify({"error": "Not implemented"}), 501
