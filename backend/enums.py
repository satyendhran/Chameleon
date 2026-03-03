from enum import Enum, auto


class AwardType(Enum):
    """Post-match awards voted on by players."""
    GOATED = auto()      
    GENERALIST = auto()  
    AARONIC = auto()     


class GameStatus(Enum):
    """Status of a Match."""
    WAITING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()


class HostType(Enum):
    """
    Determines whether the match is run by the computer or a human host.
    """
    COMPUTER = auto()
    HUMAN = auto()


class Phase(Enum):
    """Current phase within a round."""
    DISCUSSION = auto()
    VOTING = auto()
    RESULT = auto()
