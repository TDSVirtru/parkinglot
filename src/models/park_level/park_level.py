"""internal service for park level."""

from ..park import Park


class ParkLevel(Park):
    """Park level class."""

    def __init__(self, name, rows=[]):
        """Construct a ParkLevel."""
        Park.__init__(self, name, rows)
