"""
# TODO Visu
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from backend.interfaces import ReconnectHandler

if TYPE_CHECKING:
    from backend.user import User


class TimedReconnectHandler(ReconnectHandler):
    """
    Grace-period based reconnection handler.

    When a player disconnects, a countdown timer starts.
    If the player rejoins before the timer expires, the match continues normally.
    If the timer expires, the match may proceed without them or they are eliminated,
    depending on game rules.

    Attributes
    ----------
    grace_period_seconds : int
        Number of seconds a disconnected player has to rejoin.
    _pending : dict[str, float]
        Mapping of player_id → disconnect_timestamp for players in grace period.
    """

    def __init__(self, grace_period_seconds: int = 60) -> None:
        # TODO Visu
        self.grace_period_seconds: int = grace_period_seconds
        self._pending: dict[str, float] = {}

    # ------------------------------------------------------------------

    def handle_disconnect(self, player: User) -> None:
        """
        Called immediately when a player drops from the session.

        Parameters
        ----------
        player : User
            The player who disconnected.
        """
        # TODO Visu
        raise NotImplementedError

    def start_grace_period(self, player: User) -> None:
        """
        Begin the countdown timer for the disconnected player.

        Parameters
        ----------
        player : User
            The player for whom the grace period starts.

        Notes
        -----
        After grace_period_seconds elapses, this should trigger the
        game controller to decide whether to continue or eliminate the player.
        """
        # TODO Visu — start an async timer
        raise NotImplementedError

    def handle_rejoin(self, player: User) -> None:
        """
        Restore the player to the active match state after a successful rejoin.

        Parameters
        ----------
        player : User
            The player who is rejoining.

        Raises
        ------
        RuntimeError
            If the grace period has already expired for this player.
        """
        # TODO Visu
        raise NotImplementedError
