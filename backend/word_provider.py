"""
# TODO SAT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from backend.interfaces import WordProvider

if TYPE_CHECKING:
    from backend.interfaces import GameMode


class AutoWordProvider(WordProvider):
    """
    Computer-controlled word and topic generator.

    Attributes
    ----------
    _topic : str
        The topic generated for the current round (e.g., "Animals").
    _word_map : dict[str, str]
        Mapping of player_id → assigned word. Populated by generate_words().
    """

    def __init__(self) -> None:
        # TODO Satyendhran — initialise any word corpus
        self._topic: str = ""
        self._word_map: dict[str, str] = {}

    def generate_topic(self) -> str:
        """
        Generate a topic category for the upcoming round.

        Returns
        -------
        str
            A single topic string (e.g., "Animals", "Sports", "Movies").


        """
        # TODO Satyendhran
        raise NotImplementedError

    def generate_words(self, mode: GameMode) -> dict[str, str]:
        """
        Generate one word per player, adapting the distribution to the active mode.

        Parameters
        ----------
        mode : GameMode
            The current game mode instance.
            Use its name (mode.get_mode_name()) to switch word-generation strategy.

        Returns
        -------
        dict[str, str]
            Mapping of player_id → the word that player receives.
        """
        # TODO Satyendhran

        raise NotImplementedError
