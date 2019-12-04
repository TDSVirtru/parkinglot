"""internal service for park rows."""

from ..park import Park


class ParkRow(Park):
    """ParkRow class."""

    def __init__(self, name, spaces=[]):
        """Construct a park row."""
        Park.__init__(self, name, spaces)

    def park(self, car):
        """Park the car in the first acceptable spot.

        If the preferred flag is true, then only consider preferred spots.
        If the preferred flag is false(default), then park in the first
        available spot. Returns the coordinates of the space, or None if
        not successful.
        """

        
