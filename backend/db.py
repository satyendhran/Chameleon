"""
# TODO Sharvesh
"""

from __future__ import annotations

# TODO Sharvesh — import your ORM of choice, e.g.:
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
# from sqlalchemy.orm import relationship

# TODO
db = None  # type: ignore[assignment]


class UserModel:
    """
    Persistent representation of a User in the database.

    Attributes
    ----------
    user_id : str
        Primary key — UUID string.
    username : str
        Unique display name.
    password_hash : str
        Bcrypt / Argon2 hash of the password.
    """
    # TODO Sharvesh — add __tablename__, Column definitions, and relationships
    user_id: str
    username: str
    password_hash: str


class ProfileModel:
    """
    Persistent representation of a Profile in the database.

    Attributes
    ----------
    profile_id : str
        Primary key — mirrors user_id.
    wins : int
        Lifetime total wins.
    losses : int
        Lifetime total losses.
    imposter_success_rate : float
        Running success rate as imposter.
    avg_turn_duration : float
        Average seconds taken per turn across all matches.
    """
    # TODO Sharvesh — add __tablename__, Column definitions, and FK to UserModel
    profile_id: str
    wins: int
    losses: int
    imposter_success_rate: float
    avg_turn_duration: float


class RoomModel:
    """
    Persistent representation of a Room.

    Attributes
    ----------
    room_id : str
        Primary key — UUID string.
    access_code : str
        Short alphanumeric code players use to join.
    """
    # TODO Sharvesh — add __tablename__, Column definitions, and M2M relationship to UserModel
    room_id: str
    access_code: str


class LeaderboardModel:
    """
    Persistent representation of a room's leaderboard entry.

    Attributes
    ----------
    room_id : str
        FK → RoomModel.
    user_id : str
        FK → UserModel.
    score : int
        Cumulative score used for ranking.
    rank : int
        Current rank within the room.
    """
    # TODO Sharvesh — add __tablename__, Column definitions, composite PK or surrogate PK
    room_id: str
    user_id: str
    score: int
    rank: int


class MatchModel:
    """
    Persistent representation of a Match.

    Attributes
    ----------
    match_id : str
        Primary key.
    room_id : str
        FK → RoomModel.
    status : str
        Serialised GameStatus value.
    host_type : str
        Serialised HostType value.
    """
    # TODO Sharvesh — add __tablename__, Column definitions
    match_id: str
    room_id: str
    status: str
    host_type: str

def init_db(app: object) -> None:
    """
    Initialise the database with the given Flask app context.

    Parameters
    ----------
    app : Flask
        The Flask application instance.
    """
    # TODO Sharvesh
    raise NotImplementedError


def get_db_session() -> object:
    """
    Return the current DB session for query operations.

    Returns
    -------
    Session
        Active SQLAlchemy session (or equivalent).
    """
    # TODO Sharvesh
    raise NotImplementedError
