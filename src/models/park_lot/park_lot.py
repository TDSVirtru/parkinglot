"""internal service for park lots."""

from ..park import Park
from ..park_level import ParkLevel


class ParkLot(Park):
    """Park lot class."""

    @classmethod
    def create(cls, opts):
        """Unpack serialization object and return an ParkRow."""
        levels = []
        if "levels" in opts:
            for level in opts['levels']:
                levels.append(ParkLevel.create(level))

        return cls(opts['name'], levels)

    def __init__(self, name, levels=[]):
        """Construct a ParkLot."""
        Park.__init__(self, name, levels)
