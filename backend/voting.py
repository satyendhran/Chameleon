"""
# TODO Ambika
# TODO Aaron
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from backend.interfaces import VotingStrategy

if TYPE_CHECKING:
    from backend.user import User

class ModeVoting(VotingStrategy):
    """
    Voting strategy used to select the game mode before a match starts.

    All players vote on which game mode to play.
    The mode with the most votes is selected.

    Attributes
    ----------
    _votes : dict[str, int]
        Internal tally populated by collect_votes().
    """

    def __init__(self) -> None:
        # TODO Ambika — initialise any state needed before a vote round
        self._votes: dict[str, int] = {}

    # ------------------------------------------------------------------

    def collect_votes(self, options: list[str], voters: list[User]) -> dict[str, int]:
        """
        Gather one vote per player from the provided mode options.

        Parameters
        ----------
        options : list[str]
            Available game mode names to vote on.
        voters : list[User]
            Players participating in the vote.

        Returns
        -------
        dict[str, int]
            Tally of option → vote count after all voters have submitted.
        """
        # TODO Ambika
        raise NotImplementedError

    def apply_majority_rule(self) -> str:
        """
        Return the option that received the most votes.

        Returns
        -------
        str
            Winning mode name.
        """
        # TODO Ambika
        raise NotImplementedError

    def resolve_tie(self) -> str:
        """
        Break a tie among top-voted mode options.

        Returns
        -------
        str
            Winner chosen by tie-breaking logic.

        Notes
        -----
        # TODO Aaron
        """
        raise NotImplementedError

class EliminationVoting(VotingStrategy):
    """
    Voting strategy used to eliminate a player during a round.

    Attributes
    ----------
    _votes : dict[str, int]
        Internal tally populated by collect_votes().
    """

    def __init__(self) -> None:
        # TODO Ambika
        self._votes: dict[str, int] = {}

    # ------------------------------------------------------------------

    def collect_votes(self, options: list[str], voters: list[User]) -> dict[str, int]:
        """
        Gather one vote per player against the listed candidates.

        Parameters
        ----------
        options : list[str]
            Player IDs or names available to be voted against.
        voters : list[User]
            Active players who are allowed to vote.

        Returns
        -------
        dict[str, int]
            Tally of player → vote count.
        """
        # TODO Ambika
        raise NotImplementedError

    def apply_majority_rule(self) -> str:
        """
        Return the player with the most elimination votes.

        Returns
        -------
        str
            Player ID of the eliminated player.
        """
        # TODO Ambika
        raise NotImplementedError

    def resolve_tie(self) -> str:
        """
        Break a tie in elimination vote.

        Returns
        -------
        str
            Player ID chosen to be eliminated after tie-break.

        """
        # TODO Aaron        
        raise NotImplementedError


class AwardVoting(VotingStrategy):
    """
    Voting strategy used post-match to assign awards to players.
    Attributes
    ----------
    _votes : dict[str, int]
        Internal tally populated by collect_votes().
    """

    def __init__(self) -> None:
        # TODO Ambika 
        self._votes: dict[str, int] = {}

    # ------------------------------------------------------------------

    def collect_votes(self, options: list[str], voters: list[User]) -> dict[str, int]:
        """
        Gather one vote per player for the award nominees.

        Parameters
        ----------
        options : list[str]
            Player IDs or names eligible for the current award.
        voters : list[User]
            All players who participate in award voting.

        Returns
        -------
        dict[str, int]
            Tally of nominee → vote count.
        """
        # TODO Ambika
        raise NotImplementedError

    def apply_majority_rule(self) -> str:
        """
        Return the nominee with the most award votes.

        Returns
        -------
        str
            Player ID of the award winner.
        """
        # TODO Ambika
        raise NotImplementedError

    def resolve_tie(self) -> str:
        """
        Break a tie in award voting.

        Returns
        -------
        str
            Player ID chosen as award winner after tie-break.

        """
        # TODO Aaron — implement tie-breaking strategy for award voting
        raise NotImplementedError
