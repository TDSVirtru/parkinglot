"""internal service for park rows."""

from ..park import Park


class ParkRow(Park):
    """ParkRow class."""

    def __init__(self, name, spaces=[]):
        """Construct a park row."""
        Park.__init__(self, name)
        self.__spaces = set(spaces)

    @property
    def spaces(self):
        """Return a copy of the set of spaces."""
        return self.__spaces.copy()

    @spaces.setter
    def spaces(self, value):
        """Noop."""
        raise Exception("Cannot set spaces on a park row after construction.")

    def park(self, car):
        """Park the car if possible.

        Returns the coordinates of the space if successful, or None if
        the space is full or the car doesn't have the attributes required.
        """
        return None

    def is_full(self):
        """Return the full status of the row instance."""
        for space in self.__spaces:
            if space.is_empty():
                return False
        return True

    def is_empty(self):
        """Return the empty status of the row instance."""
        for space in self.__spaces:
            if space.is_full():
                return False
        return True
