"""
# TODO Kaarthik
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from backend.enums import AwardType, GameStatus, HostType, Phase

if TYPE_CHECKING:
    from backend.user import User
    from backend.game_modes import ImposterMode  


class Turn:
    """
    One player's action during a single round.

    Attributes
    ----------
    player_id : str
        ID of the player whose turn this is.
    response : str
        The word or phrase the player submitted.
    timestamp : float
        Unix epoch seconds when the turn was submitted.
    locked : bool
        True once submit_response has been called; no further edits allowed.
    """

    def __init__(self, player_id: str) -> None:
        # TODO Kaarthik — link to the parent Round
        self.player_id: str = player_id
        self.response: str = ""
        self.timestamp: float = 0.0
        self.locked: bool = False

    def submit_response(self, response: str) -> None:
        """
        Record the player's response and lock the turn.

        Parameters
        ----------
        response : str
            The word or phrase the player chose to say this round.

        Raises
        ------
        RuntimeError
            If the turn is already locked.
        """
        # TODO Kaarthik
        raise NotImplementedError

    def lock_turn(self) -> None:
        """
        Permanently lock this turn so no further changes can be made.

        Raises
        ------
        RuntimeError
            If the turn is already locked.
        """
        # TODO Kaarthik
        raise NotImplementedError

class Round:
    """
    One full cycle of play in which every active player takes a turn.

    Attributes
    ----------
    round_number : int
        1-based index of this round within its parent match.
    duration_seconds : int
        Wall-clock time this round lasted.
    turns : list[Turn]
        One Turn per active player, in play order.
    """

    def __init__(self, round_number: int) -> None:
        # TODO Kaarthik — link to parent Match, initialise turns list from active players
        self.round_number: int = round_number
        self.duration_seconds: int = 0
        self.turns: list[Turn] = []

    def start(self) -> None:
        """
        Mark this round as started and begin collecting turns.

        Notes
        -----
        Should notify all active players that their turn window is open.
        """
        # TODO Kaarthik
        raise NotImplementedError

    def end(self) -> None:
        """
        Close this round, lock all pending turns, and record duration.

        Notes
        -----
        Triggers the transition to the VOTING phase.
        """
        # TODO Kaarthik
        raise NotImplementedError

    def get_turns(self) -> list[Turn]:
        """
        Return all turns taken during this round.

        Returns
        -------
        list[Turn]
            Turns in submission order.
        """
        # TODO Kaarthik
        raise NotImplementedError

class MatchResult:
    """
    Immutable record of how a match concluded.

    Attributes
    ----------
    winning_role : str
        The role that won.
    winning_players : list[User]
        Players who belong to the winning role.
    awards : dict[str, AwardType]
        Mapping of player_id → award earned.
    """

    def __init__(
        self,
        winning_role: str,
        winning_players: list[User],
        awards: dict[str, AwardType],
    ) -> None:
        self.winning_role: str = winning_role
        self.winning_players: list[User] = winning_players
        self.awards: dict[str, AwardType] = awards


class GameState:
    """
    Live snapshot of what is happening in the match right now.

    Attributes
    ----------
    current_round : int
        1-based index of the round currently in progress.
    phase : Phase
        Current phase within the round (DISCUSSION, VOTING, RESULT).
    active_players : list[User]
        Players still in the game (not eliminated).
    eliminated_players : list[User]
        Players who have been voted out.
    """

    def __init__(self, players: list[User]) -> None:
        # TODO Kaarthik — initialise from the Match's player list
        self.current_round: int = 1
        self.phase: Phase = Phase.DISCUSSION
        self.active_players: list[User] = list(players)
        self.eliminated_players: list[User] = []

    def update_state(self) -> None:
        """
        Advance the state after a phase or round event (e.g., elimination).
        """
        # TODO Kaarthik
        raise NotImplementedError

    def is_match_over(self) -> bool:
        """
        Determine whether the match-ending condition has been met.

        Returns
        -------
        bool
            True if the match should end immediately.
        """
        # TODO Kaarthik
        raise NotImplementedError

class Match:
    """
    A single full game session within a Room.

    Attributes
    ----------
    match_id : str
        Unique identifier for this match.
    status : GameStatus
        Lifecycle state (WAITING → IN_PROGRESS → COMPLETED).
    players : list[User]
        All players who joined this match.
    host_type : HostType
        Whether a GameController or a HumanHost is running things.
    mode : object or None
        The active GameMode instance (set when the match starts).
    game_state : GameState or None
        Live state tracker (created when the match starts).
    rounds : list[Round]
        Rounds that have been completed or are in progress.
    result : MatchResult or None
        Set when the match completes.
    """

    def __init__(
        self,
        match_id: str,
        players: list[User],
        host_type: HostType,
    ) -> None:
        # TODO Kaarthik — persist to DB, link to parent Room
        self.match_id: str = match_id
        self.status: GameStatus = GameStatus.WAITING
        self.players: list[User] = players
        self.host_type: HostType = host_type
        self.mode: object | None = None
        self.game_state: GameState | None = None
        self.rounds: list[Round] = []
        self.result: MatchResult | None = None

    # ------------------------------------------------------------------

    def start(self) -> None:
        """
        Transition the match from WAITING to IN_PROGRESS.

        Notes
        -----
        Should create the first Round and notify all players.
        """
        # TODO Kaarthik 
        raise NotImplementedError

    def end(self) -> None:
        """
        Finalise the match, resolve awards, and log the result.

        Notes
        -----
        Sets status=COMPLETED and triggers analytics updates.
        """
        # TODO Kaarthik
        raise NotImplementedError

    def get_rounds(self) -> list[Round]:
        """
        Return all rounds associated with this match.

        Returns
        -------
        list[Round]
            Rounds in chronological order.
        """
        # TODO Kaarthik
        raise NotImplementedError

    def get_result(self) -> MatchResult | None:
        """
        Return the final result of this match.

        Returns
        -------
        MatchResult or None
            None if the match has not ended yet.
        """
        # TODO Kaarthik
        raise NotImplementedError
