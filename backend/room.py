"""
# TODO Sharvesh
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from backend.enums import HostType

if TYPE_CHECKING:
    from backend.user import User
    from backend.match import Match

class Leaderboard:
    """
    Per-room ranking table, updated after every match.

    Attributes
    ----------
    room_id : str
        The room this leaderboard belongs to.
    rankings : dict[str, int]
        Mapping of user_id → cumulative score.
    """

    def __init__(self, room_id: str) -> None:
        # TODO Sharvesh — load from DB if already exists
        self.room_id: str = room_id
        self.rankings: dict[str, int] = {}   # user_id → score

    # ------------------------------------------------------------------

    def update_rankings(self) -> None:
        """
        Recalculate and persist all rankings based on current scores.
        """
        # TODO Sharvesh
        raise NotImplementedError

    def get_top_players(self, n: int) -> list[User]:
        """
        Return the top-n players by score.

        Parameters
        ----------
        n : int
            Number of top players to return.

        Returns
        -------
        list[User]
            Ordered list of User objects (highest score first).
        """
        # TODO Sharvesh
        raise NotImplementedError


class Room:
    """
    A persistent game room that hosts multiple matches over time.

    Attributes
    ----------
    room_id : str
        Unique identifier for this room (UUID or short code).
    access_code : str
        Short code players use to join the room.
    members : list[User]
        Players currently in this room.
    leaderboard : Leaderboard
        The room's ranking table.
    match_history : list[Match]
        All matches that have taken place in this room.
    """

    def __init__(self, room_id: str, access_code: str) -> None:
        # TODO Sharvesh — load from DB if already exists
        self.room_id: str = room_id
        self.access_code: str = access_code
        self.members: list[User] = []
        self.leaderboard: Leaderboard = Leaderboard(room_id=room_id)
        self.match_history: list[Match] = []

    # ------------------------------------------------------------------

    def add_member(self, user: User) -> None:
        """
        Add a player to this room.

        Parameters
        ----------
        user : User
            The player to add.

        Raises
        ------
        ValueError
            If the user is already a member.
        """
        # TODO Sharvesh
        raise NotImplementedError

    def remove_member(self, user: User) -> None:
        """
        Remove a player from this room.

        Parameters
        ----------
        user : User
            The player to remove.

        Raises
        ------
        ValueError
            If the user is not a member of this room.
        """
        # TODO Sharvesh
        raise NotImplementedError

    def create_match(self, host_type: HostType) -> Match:
        """
        Instantiate a new match within this room.

        Parameters
        ----------
        host_type : HostType
            Whether to use a GameController or HumanHost.

        Returns
        -------
        Match
            A freshly created match, stored in match_history.
        """
        # TODO Sharvesh
        raise NotImplementedError

    def get_leaderboard(self) -> Leaderboard:
        """
        Return the room's current leaderboard.

        Returns
        -------
        Leaderboard
            The leaderboard object for this room.
        """
        # TODO Sharvesh
        raise NotImplementedError

    def get_match_history(self) -> list[Match]:
        """
        Return all matches played in this room.

        Returns
        -------
        list[Match]
            Match history, most recent first.
        """
        # TODO Sharvesh
        raise NotImplementedError
