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
        self.__parks = set(parks)  # order ignored. Can be replaced with List.

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

    # Override the Park.park method.
    def park(self, car, preferred=False):
        """Park the car in the first acceptable spot.

        If the preferred flag is true, then only consider preferred spots.
        If the preferred flag is false(default), then park in the first
        available spot. Returns the coordinates of the space, or None if
        not successful.
        """
        for park in self.__parks:
            result = park.park(car, preferred)
            if result is not None:
                return "{0}-{1}".format(self.name, result)
        return None

    # Override the Park.is_full method.
    def is_full(self):
        """Return the full status of this park instance."""
        for park in self.parks:
            if park.is_empty():
                return False
        return True

    # Override the Park.is_empty method.
    def is_empty(self):
        """Return the empty status of this park instance."""
        for park in self.parks:
            if park.is_full():
                return False
        return True
