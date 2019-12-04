"""internal service for park rows."""

from ..park import Park


class ParkRow(Park):
    """ParkRow class."""

    def __init__(self, name, spaces=[]):
        """Construct a park row."""
        Park.__init__(self, name, spaces)
