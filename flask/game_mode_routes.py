"""
# TODO Jayant
"""

from __future__ import annotations

from flask import Blueprint, request, jsonify

game_mode_bp = Blueprint("game_mode", __name__, url_prefix="/api/modes")

@game_mode_bp.route("/", methods=["GET"])
def list_modes():
    """
    Return a list of all available game modes.

    Returns
    -------
    JSON
        ``{"modes": ["Imposter", "Imposter Jester", "Apples & Pears", "Surprise"]}``
    """
    # TODO Jayant
    return jsonify({"error": "Not implemented"}), 501

@game_mode_bp.route("/<mode_name>", methods=["GET"])
def get_mode_info(mode_name: str):
    """
    Return description and win conditions for a specific mode.

    Parameters
    ----------
    mode_name : str
        Path parameter — the name of the game mode (URL-encoded).

    Returns
    -------
    JSON
        ``{"mode_name": "...", "win_condition": "..."}``
    """
    # TODO Jayant
    return jsonify({"error": "Not implemented"}), 501

@game_mode_bp.route("/vote", methods=["POST"])
def vote_for_mode():
    """
    Submit a player's mode vote before a match begins.

    Request Body (JSON)
    -------------------
    match_id : str
        The match in the pre-game lobby.
    mode_name : str
        The mode the player is voting for.

    Returns
    -------
    JSON
        ``{"message": "vote recorded"}`` on success.
        ``{"mode_selected": "<name>"}`` when all players have voted and a winner is decided.
    """
    # TODO Jayant
    return jsonify({"error": "Not implemented"}), 501


@game_mode_bp.route("/<match_id>/select", methods=["POST"])
def host_select_mode(match_id: str):
    """
    Human host directly selects the mode (bypasses voting).

    Parameters
    ----------
    match_id : str
        Path parameter.

    Request Body (JSON)
    -------------------
    mode_name : str
        The mode chosen by the human host.

    Returns
    -------
    JSON
        ``{"mode_selected": "<name>"}`` on success.
    """
    # TODO Jayant
    return jsonify({"error": "Not implemented"}), 501
