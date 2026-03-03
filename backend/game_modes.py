"""
# TODO Jayant
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from backend.interfaces import GameMode

if TYPE_CHECKING:
    from backend.user import User

class ImposterMode(GameMode):
    """
    Classic imposter mode.
    """

    def assign_roles(self, players: list[User]) -> None:
        """
        Assign one ImposterRole and the rest MajorityRoles.

        Parameters
        ----------
        players : list[User]
            All players joining this match.
        """
        # TODO Jayant
        raise NotImplementedError

    def get_win_condition(self) -> str:
        """
        Return the win conditions for this mode.

        Returns
        -------
        str
            Human-readable description.
        """
        # TODO Jayant
        raise NotImplementedError

    def apply_special_rules(self) -> None:
        """Apply ImposterMode-specific rule hooks (e.g., word difference logic)."""
        # TODO Jayant
        raise NotImplementedError

    def get_mode_name(self) -> str:
        """
        Return the display name for this mode.

        Returns
        -------
        str
            "Imposter"
        """
        # TODO Jayant
        raise NotImplementedError

class ImposterJesterMode(GameMode):
    """
    Imposter + Jester hybrid mode.
    """

    def assign_roles(self, players: list[User]) -> None:
        """
        Assign one ImposterRole, one JesterRole, and MajorityRoles to the rest.

        Parameters
        ----------
        players : list[User]
            All players joining this match.
        """
        # TODO Jayant
        raise NotImplementedError

    def get_win_condition(self) -> str:
        """
        Return the win conditions for this mode.

        Returns
        -------
        str
            Human-readable multi-role description.
        """
        # TODO Jayant
        raise NotImplementedError

    def apply_special_rules(self) -> None:
        """Apply ImposterJesterMode-specific rule hooks (e.g., Jester win detection)."""
        # TODO Jayant
        raise NotImplementedError

    def get_mode_name(self) -> str:
        """
        Return the display name for this mode.

        Returns
        -------
        str
            "Imposter Jester"
        """
        # TODO Jayant
        raise NotImplementedError


class ApplesPearsMode(GameMode):
    """
    Apples & Pears mode.
    """

    def assign_roles(self, players: list[User]) -> None:
        """
        Assign majority roles to all; mark one player as the odd-one-out.

        Parameters
        ----------
        players : list[User]
            All players joining this match.
        """
        # TODO Jayant
        raise NotImplementedError

    def get_win_condition(self) -> str:
        """
        Return the win conditions for this mode.

        Returns
        -------
        str
            Human-readable description.
        """
        # TODO Jayant
        raise NotImplementedError

    def apply_special_rules(self) -> None:
        """Apply ApplesPearsMode-specific word-difference logic."""
        # TODO Jayant
        raise NotImplementedError

    def get_mode_name(self) -> str:
        """
        Return the display name for this mode.

        Returns
        -------
        str
            "Apples & Pears"
        """
        # TODO Jayant
        raise NotImplementedError

class SurpriseMode(GameMode):
    """
    Surprise mode

    Attributes
    ----------
    delegate_to : GameMode or None
        The randomly chosen GameMode instance. None until select_delegate() is called.
    """

    def __init__(self) -> None:
        # TODO Jayant
        self.delegate_to: GameMode | None = None

    # ------------------------------------------------------------------

    def select_delegate(self) -> None:
        """
        Randomly pick one of [ImposterMode, ImposterJesterMode, ApplesPearsMode]
        and assign it to self.delegate_to.
        """
        # TODO Jayant
        raise NotImplementedError

    def assign_roles(self, players: list[User]) -> None:
        """
        Delegate role assignment to the chosen mode.

        Parameters
        ----------
        players : list[User]
            All players joining this match.

        Raises
        ------
        RuntimeError
            If select_delegate() has not been called yet.
        """
        # TODO Jayant
        raise NotImplementedError

    def get_win_condition(self) -> str:
        """
        Return the win condition of the chosen delegate mode.

        Returns
        -------
        str
            Delegated win condition string.
        """
        # TODO Jayant
        raise NotImplementedError

    def apply_special_rules(self) -> None:
        """Forward special-rule logic to the delegate."""
        # TODO Jayant
        raise NotImplementedError

    def get_mode_name(self) -> str:
        """
        Return the mode name of the chosen delegate.

        Returns
        -------
        str
            Delegated mode name (e.g., "Imposter").
        """
        # TODO Jayant
        raise NotImplementedError
