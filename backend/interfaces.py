from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.enums import AwardType
    from typing import Any  


class Host(ABC):
    """Interface for anything that can run a match."""

    @abstractmethod
    def select_mode(self) -> GameMode:
        """
        Choose the game mode for the upcoming match.

        Returns
        -------
        GameMode
            The selected game mode instance.
        """
        ...

    @abstractmethod
    def assign_roles(self, players: list) -> None:
        """
        Assign roles to all players before the match starts.

        Parameters
        ----------
        players : list[User]
            Active players joining the match.
        """
        ...

    @abstractmethod
    def start_match(self, match: Any) -> None:
        """
        Kick off the match lifecycle.

        Parameters
        ----------
        match : Match
            The match object to start.
        """
        ...


class GameMode(ABC):
    """Interface for all game modes. Add a new mode = new class, nothing else."""

    @abstractmethod
    def assign_roles(self, players: list) -> None:
        """
        Distribute role objects to players according to this mode's rules.

        Parameters
        ----------
        players : list[User]
            Players participating in this match.
        """
        ...

    @abstractmethod
    def get_win_condition(self) -> str:
        """
        Human-readable description of how a player wins in this mode.

        Returns
        -------
        str
            Win condition description.
        """
        ...

    @abstractmethod
    def apply_special_rules(self) -> None:
        """Apply any mode-specific rule overrides or hooks."""
        ...

    @abstractmethod
    def get_mode_name(self) -> str:
        """
        Return the display name for this mode.

        Returns
        -------
        str
            Mode name
        """
        ...

class Role(ABC):
    """Interface for all role types assigned to players."""

    @abstractmethod
    def get_role_name(self) -> str:
        """
        Return the display name of this role.

        Returns
        -------
        str
            Role name.
        """
        ...

    @abstractmethod
    def get_win_condition(self) -> str:
        """
        Return the win condition for this role.

        Returns
        -------
        str
            Win condition description.
        """
        ...

class VotingStrategy(ABC):
    """
    Interface for all vote types.
    """

    @abstractmethod
    def collect_votes(self, options: list[str], voters: list) -> dict[str, int]:
        """
        Gather one vote per voter from the provided options.

        Parameters
        ----------
        options : list[str]
            Votable options (player names, mode names, etc.).
        voters : list[User]
            Players who are allowed to vote.

        Returns
        -------
        dict[str, int]
            Mapping of option → vote count.
        """
        ...

    @abstractmethod
    def apply_majority_rule(self) -> str:
        """
        Determine the winner from collected votes using simple majority.

        Returns
        -------
        str
            The option that received the most votes.
        """
        ...

    @abstractmethod
    def resolve_tie(self) -> str:
        """
        Break a tie when two or more options share the top vote count.

        Returns
        -------
        str
            The chosen option after tie-breaking.
        """
        ...

class WordProvider(ABC):
    """Interface for generating topics and per-player words."""

    @abstractmethod
    def generate_topic(self) -> str:
        """
        Generate a topic category for the round.

        Returns
        -------
        str
            Topic string
        """
        ...

    @abstractmethod
    def generate_words(self, mode: GameMode) -> dict[str, str]:
        """
        Generate one word per player, adjusted to the active game mode.

        Parameters
        ----------
        mode : GameMode
            The active game mode

        Returns
        -------
        dict[str, str]
            Mapping of player_id → assigned word.
        """
        ...

class AwardStrategy(ABC):
    """Interface for the end-of-match award pipeline."""

    @abstractmethod
    def nominate_awards(self, match: Any) -> None:
        """
        Determine which players are eligible for each award.

        Parameters
        ----------
        match : Match
            Completed match to analyse.
        """
        ...

    @abstractmethod
    def collect_award_votes(self, voters: list) -> None:
        """
        Run the award voting round.

        Parameters
        ----------
        voters : list[User]
            Players allowed to vote on awards.
        """
        ...

    @abstractmethod
    def assign_awards(self) -> dict[str, "AwardType"]:
        """
        Finalise and return the award assignments.

        Returns
        -------
        dict[str, AwardType]
            Mapping of player_id → AwardType.
        """
        ...

class ReconnectHandler(ABC):
    """Interface for handling player disconnects and rejoins mid-match."""

    @abstractmethod
    def handle_disconnect(self, player: Any) -> None:
        """
        Called immediately when a player disconnects.

        Parameters
        ----------
        player : User
            The disconnected player.
        """
        ...

    @abstractmethod
    def start_grace_period(self, player: Any) -> None:
        """
        Begin the countdown timer allowing the player to rejoin.

        Parameters
        ----------
        player : User
            Player for whom the grace period is started.
        """
        ...

    @abstractmethod
    def handle_rejoin(self, player: Any) -> None:
        """
        Restore the player to the active match after a successful rejoin.

        Parameters
        ----------
        player : User
            The rejoining player.
        """
        ...


# ---------------------------------------------------------------------------
# AnalyticsService interface — implemented by MatchAnalyticsService
# ---------------------------------------------------------------------------

class AnalyticsService(ABC):
    """Interface for tracking per-player and room-level statistics."""

    @abstractmethod
    def track_win(self, player: Any) -> None:
        """
        Record a win for the given player.

        Parameters
        ----------
        player : User
            The winning player.
        """
        ...

    @abstractmethod
    def track_loss(self, player: Any) -> None:
        """
        Record a loss for the given player.

        Parameters
        ----------
        player : User
            The losing player.
        """
        ...

    @abstractmethod
    def track_award(self, player: Any, award: "AwardType") -> None:
        """
        Record an award earned by the player.

        Parameters
        ----------
        player : User
            Player who earned the award.
        award : AwardType
            The award type earned.
        """
        ...

    @abstractmethod
    def track_turn_duration(self, turn: Any) -> None:
        """
        Record how long a player took on their turn.

        Parameters
        ----------
        turn : Turn
            The completed turn object.
        """
        ...

    @abstractmethod
    def update_leaderboard(self, room: Any) -> None:
        """
        Recalculate and persist leaderboard rankings for the room.

        Parameters
        ----------
        room : Room
            The room whose leaderboard needs updating.
        """
        ...

    @abstractmethod
    def get_imposter_success_rate(self, player: Any) -> float:
        """
        Calculate what fraction of imposter roles this player survived.

        Parameters
        ----------
        player : User
            The player to query.

        Returns
        -------
        float
            Success rate in [0.0, 1.0].
        """
        ...
