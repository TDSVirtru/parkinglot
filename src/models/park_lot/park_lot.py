"""internal service for park lots."""

from ..park import Park


class ParkLot(Park):
    """Park lot class."""

    def __init__(self, name, levels=[]):
        """Construct a ParkLot."""
        Park.__init__(self, name, levels)
