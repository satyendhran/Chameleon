"""
# TODO Ambika
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from backend.enums import AwardType
from backend.interfaces import AwardStrategy

if TYPE_CHECKING:
    from backend.user import User
    from backend.match import Match


class StandardAwardStrategy(AwardStrategy):
    """
    Default post-match award pipeline.

    Pipeline steps
    --------------
    1. nominate_awards(match)       — determine award-eligible candidates
    2. collect_award_votes(voters)  — run AwardVoting for each AwardType
    3. assign_awards()              — return the final award assignments

    Attributes
    ----------
    _nominations : dict[AwardType, list[str]]
        Mapping of award type → list of candidate player IDs.
    _award_votes : dict[AwardType, dict[str, int]]
        Tally of votes per award per candidate.
    _final_awards : dict[str, AwardType]
        Resolved mapping of player_id → AwardType (populated by assign_awards).
    """

    def __init__(self) -> None:
        # TODO Ambika
        self._nominations: dict[AwardType, list[str]] = {}
        self._award_votes: dict[AwardType, dict[str, int]] = {}
        self._final_awards: dict[str, AwardType] = {}

    # ------------------------------------------------------------------

    def nominate_awards(self, match: Match) -> None:
        """
        Analyse the completed match and build candidate lists for each award.

        Parameters
        ----------
        match : Match
            The finished match to review.

        Notes
        -----
        GOATED     — best overall performance
        GENERALIST — most adaptable across different roles.
        AARONIC    — most notably Aaronic moment of the match.
        """
        # TODO Ambika
        raise NotImplementedError

    def collect_award_votes(self, voters: list[User]) -> None:
        """
        Run one AwardVoting round per AwardType and store the tallies.

        Parameters
        ----------
        voters : list[User]
            All players eligible to vote on awards.
        """
        # TODO Ambika
        raise NotImplementedError

    def assign_awards(self) -> dict[str, AwardType]:
        """
        Resolve each award vote and return the final assignments.

        Returns
        -------
        dict[str, AwardType]
            Mapping of player_id → AwardType.

        Notes
        -----
        One player can receive at most one award.
        """
        # TODO Ambika
        raise NotImplementedError
