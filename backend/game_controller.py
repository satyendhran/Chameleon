"""
# TODO Visu
# TODO Jayant
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from backend.interfaces import (
    Host,
    GameMode,
    VotingStrategy,
    WordProvider,
    AwardStrategy,
    ReconnectHandler,
    AnalyticsService,
)

if TYPE_CHECKING:
    from backend.user import User
    from backend.match import Match, MatchResult

class GameController(Host):
    """
    The default neutral host that runs a match automatically.

    Attributes
    ----------
    voting_strategy : VotingStrategy
        Strategy used for mode selection and elimination votes.
    word_provider : WordProvider
        Generates the topic and per-player words.
    award_strategy : AwardStrategy
        Runs post-match award nomination and voting.
    reconnect_handler : ReconnectHandler
        Manages player disconnects and rejoins.
    analytics_service : AnalyticsService
        Tracks stats and updates leaderboards.
    """

    def __init__(
        self,
        voting_strategy: VotingStrategy,
        word_provider: WordProvider,
        award_strategy: AwardStrategy,
        reconnect_handler: ReconnectHandler,
        analytics_service: AnalyticsService,
    ) -> None:
        # TODO Visu — store the injected dependencies
        self.voting_strategy: VotingStrategy = voting_strategy
        self.word_provider: WordProvider = word_provider
        self.award_strategy: AwardStrategy = award_strategy
        self.reconnect_handler: ReconnectHandler = reconnect_handler
        self.analytics_service: AnalyticsService = analytics_service

    def select_mode(self) -> GameMode:
        """
        Run a mode vote among players and return the chosen GameMode.

        Returns
        -------
        GameMode
            The winning game mode instance.
        """
        # TODO Visu
        raise NotImplementedError

    def assign_roles(self, players: list[User]) -> None:
        """
        Delegate role assignment to the active GameMode.

        Parameters
        ----------
        players : list[User]
            Active players in the match.
        """
        # TODO Visu
        raise NotImplementedError

    def start_match(self, match: Match) -> None:
        """
        Orchestrate the full match lifecycle from start to finish.

        Parameters
        ----------
        match : Match
            The match object to run.


        """
        # TODO Visu
        raise NotImplementedError

    def conduct_elimination_voting(self) -> None:
        """
        Run an elimination vote and remove the top-voted player from GameState.

        Notes
        -----
        Uses EliminationVoting strategy. Calls resolve_tie if needed.
        """
        # TODO Visu
        raise NotImplementedError

    def determine_winner(self) -> MatchResult:
        """
        Evaluate the current GameState to decide which role/team has won.

        Returns
        -------
        MatchResult
            Populated MatchResult with winning role, players, and awards.
        """
        # TODO Visu
        raise NotImplementedError

    def log_match(self, match:Match) -> None:
        """
        Persist the match record to the database.

        Parameters
        ----------
        match : Match
            The completed match to log.
        """
        # TODO Visu
        raise NotImplementedError

    def update_analytics(self) -> None:
        """
        Push post-match stats to analytics service and update leaderboards.
        """
        # TODO Visu
        raise NotImplementedError

class HumanHost(Host):
    """
    Replaces GameController for one match when a human takes the host role.

    Attributes
    ----------
    host_player : User
        The player who has taken the host role.
    """

    def __init__(self, host_player: User) -> None:
        # TODO Jayant
        self.host_player: User = host_player

    # ------------------------------------------------------------------

    def select_mode(self) -> GameMode:
        """
        Allow the human host to manually pick the game mode.

        Returns
        -------
        GameMode
            The GameMode instance chosen by the host.
        """
        # TODO Jayant
        raise NotImplementedError

    def assign_roles(self, players: list[User]) -> None:
        """
        Allow the human host to manually assign roles to each player.

        Parameters
        ----------
        players : list[User]
            Players to assign roles to.
        """
        # TODO Jayant
        raise NotImplementedError

    def random_assign_roles(self, players: list[User]) -> None:
        """
        Randomly distribute roles, bypassing manual assignment.

        Parameters
        ----------
        players : list[User]
            Players to assign roles to.
        """
        # TODO Jayant
        raise NotImplementedError

    def start_match(self, match: Match) -> None:
        """
        Hand control to the match object after mode and roles are set.

        Parameters
        ----------
        match : Match
            The match to start.
        """
        # TODO Jayant
        raise NotImplementedError
