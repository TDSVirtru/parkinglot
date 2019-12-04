"""internal service for park rows."""

from ..park import Park
from ..park_space import ParkSpace


class ParkRow(Park):
    """ParkRow class."""

    @classmethod
    def create(cls, opts):
        """Unpack serialization object and return an ParkRow."""
        spaces = []
        if "spaces" in opts:
            for space in opts['spaces']:
                spaces.append(ParkSpace.create(space))

        return cls(opts['name'], spaces)

    def __init__(self, name, spaces=[]):
        """Construct a park row."""
        Park.__init__(self, name, spaces)
