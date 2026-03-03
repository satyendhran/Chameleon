"""
# TODO Jayant 
"""

from __future__ import annotations

from backend.interfaces import Role

class MajorityRole(Role):
    """
    The default role assigned to non-imposter players.

    Win condition: Successfully vote out the Imposter before being tricked.
    """

    def get_role_name(self) -> str:
        """
        Return the display name of this role.

        Returns
        -------
        str
            "Majority"
        """
        # TODO Jayant
        raise NotImplementedError

    def get_win_condition(self) -> str:
        """
        Return the win condition for Majority players.

        Returns
        -------
        str
            "Vote out the Imposter before the match ends."
        """
        # TODO Jayant
        raise NotImplementedError

class ImposterRole(Role):
    """
    The secret antagonist.

    Attributes
    ----------
    secret_word : str
        The different word the Imposter receives. Used in guess_word().
    """

    def __init__(self) -> None:
        # TODO Jayant
        self.secret_word: str = ""

    def get_role_name(self) -> str:
        """
        Return the display name of this role.

        Returns
        -------
        str
            "Imposter"
        """
        # TODO Jayant — return "Imposter"
        raise NotImplementedError

    def get_win_condition(self) -> str:
        """
        Return the win condition for the Imposter.

        Returns
        -------
        str
            Description covering both survival and word-guess paths.
        """
        # TODO Jayant
        raise NotImplementedError

    def guess_word(self, word: str) -> bool:
        """
        Attempt to guess the majority players' word.

        Parameters
        ----------
        word : str
            The word the Imposter thinks the majority received.

        Returns
        -------
        bool
            True if the guess matches the actual group word, False otherwise.
        """
        # TODO Jayant
        raise NotImplementedError

class JesterRole(Role):
    """
    The trickster role (only present in ImposterJesterMode).
    """

    def get_role_name(self) -> str:
        """
        Return the display name of this role.

        Returns
        -------
        str
            "Jester"
        """
        # TODO Jayant 
        raise NotImplementedError

    def get_win_condition(self) -> str:
        """
        Return the win condition for the Jester.

        Returns
        -------
        str
            "Get voted out by the majority during elimination."
        """
        # TODO Jayant
        raise NotImplementedError
