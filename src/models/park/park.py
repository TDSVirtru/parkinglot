"""Abstract base class for all Park objects."""


from ..adjudicator import Adjudicator


class Park:
    """Park class."""

    # Create a class variable to hold the singleton Adjudicator for all parks
    adjudicator = Adjudicator()

    def __init__(self, name=None, parks=[]):
        """Construct a park."""
        if name is None:
            raise Exception("Park children must have names.")
        self.__name = name
        self.__parks = set(parks)

    @property
    def name(self):
        """Return the name of the park instance."""
        return self.__name

    @name.setter
    def name(self, value):
        """Raise error. Name setting is forbidden."""
        raise Exception("The Name of a park is immutable.")

    @property
    def parks(self):
        """Return a copy of the set of parks for this node."""
        return self.__parks.copy()

    @parks.setter
    def parks(self, value):
        """Noop."""
        raise Exception("Cannot set parks on a park row after construction.")

    def park(self, car, preferred=False):
        """Park the car in the first acceptable spot.

        If the preferred flag is true, then only consider preferred spots.
        If the preferred flag is false(default), then park in the first
        available spot. Returns the coordinates of the space, or None if
        not successful.
        """
        raise Exception("Park.park method not implemented")

    def is_full():
        """Return the full status of the park instance."""
        raise Exception("Park.full method not implemented")

    def is_empty():
        """Return the empty status of the park instance."""
        raise Exception("Park.empty method not implemented")
