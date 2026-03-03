"""
# TODO Jishnu
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from backend.enums import AwardType

if TYPE_CHECKING:
    from backend.room import Room
    from backend.match import Match

@dataclass
class GlobalStats:
    """
    Aggregate lifetime statistics for a player across all rooms.

    Attributes
    ----------
    wins : int
        Total number of matches won.
    losses : int
        Total number of matches lost.
    awards_earned : list[AwardType]
        All post-match awards the player has received.
    imposter_success_rate : float
        Fraction of imposter roles where the player avoided elimination, in [0.0, 1.0].
    avg_turn_duration : float
        Average time (in seconds) a player takes per turn.
    """
    wins: int = 0
    losses: int = 0
    awards_earned: list[AwardType] = field(default_factory=list)
    imposter_success_rate: float = 0.0
    avg_turn_duration: float = 0.0

@dataclass
class RoomStats:
    """
    Per-room statistics for a single player.

    Attributes
    ----------
    room_id : str
        Identifier of the room this stat block belongs to.
    wins : int
        Wins recorded within this room.
    losses : int
        Losses recorded within this room.
    ranking : int
        Current leaderboard rank within this room.
    """
    room_id: str = ""
    wins: int = 0
    losses: int = 0
    ranking: int = 0

class Profile:
    """
    Aggregated statistics and history for one User.

    Attributes
    ----------
    profile_id : str
        Unique identifier for this profile record.
    global_stats : GlobalStats
        Lifetime aggregated stats.
    room_stats : list[RoomStats]
        Per-room stat breakdowns.
    """

    def __init__(self, profile_id: str) -> None:
        # TODO Jishnu — initialise from DB if profile_id already exists
        self.profile_id: str = profile_id
        self.global_stats: GlobalStats = GlobalStats()
        self.room_stats: list[RoomStats] = []


    def get_global_stats(self) -> GlobalStats:
        """
        Retrieve the player's lifetime aggregated statistics.

        Returns
        -------
        GlobalStats
            The global stats object.
        """
        # TODO Jishnu
        raise NotImplementedError

    def get_room_stats(self, room: Room) -> RoomStats | None:
        """
        Retrieve this player's statistics within a specific room.

        Parameters
        ----------
        room : Room
            The room to look up.

        Returns
        -------
        RoomStats or None
            The room stats block, or None if the player has no history in this room.
        """
        # TODO Jishnu
        raise NotImplementedError

    def get_match_history(self) -> list[Match]:
        """
        Retrieve the ordered list of matches this player participated in.

        Returns
        -------
        list[Match]
            Match history, most recent first.
        """
        # TODO Jishnu
        raise NotImplementedError

class User:
    """
    A registered player in the Chameleon system.

    Attributes
    ----------
    user_id : str
        Unique identifier (UUID or DB primary key).
    username : str
        Display name chosen at registration.
    password_hash : str
        Hashed password; never store plaintext.
    profile : Profile
        The user's profile, created automatically on registration.
    joined_rooms : list[Room]
        Rooms this user is currently a member of.
    """

    def __init__(
        self,
        user_id: str,
        username: str,
        password_hash: str,
    ) -> None:
        # TODO Jishnu — validate user_id uniqueness before construction
        self.user_id: str = user_id
        self.username: str = username
        self.password_hash: str = password_hash
        self.profile: Profile = Profile(profile_id=user_id)
        self.joined_rooms: list[Room] = []

    # ------------------------------------------------------------------

    def register(self) -> None:
        """
        Persist this user to the database for the first time.

        Raises
        ------
        ValueError
            If the username is already taken.
        """
        # TODO Jishnu
        raise NotImplementedError

    def login(self, plain_password: str) -> bool:
        """
        Verify credentials and return whether the login succeeded.

        Parameters
        ----------
        plain_password : str
            The raw password submitted by the user.

        Returns
        -------
        bool
            True if credentials are valid, False otherwise.
        """
        # TODO Jishnu
        raise NotImplementedError

    def get_profile(self) -> Profile:
        """
        Return the user's profile object.

        Returns
        -------
        Profile
            This user's profile.
        """
        # TODO Jishnu
        raise NotImplementedError

    def get_joined_rooms(self) -> list[Room]:
        """
        Return all rooms the user is a member of.

        Returns
        -------
        list[Room]
            Rooms this user belongs to.
        """
        # TODO Jishn
        raise NotImplementedError
