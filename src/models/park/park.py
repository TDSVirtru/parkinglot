"""Abstract base class for all Park objects."""


from ..adjudicator import Adjudicator


class Park:
    """Park class."""

    # Create a class variable to hold the singleton Adjudicator for all parks
    adjudicator = Adjudicator()

    def __init__(self, name=None):
        """Construct a park."""
        if name is None:
            raise Exception("Park children must have names.")
        self.__name = name

    @property
    def name(self):
        """Return the name of the park instance."""
        return self.__name

    @name.setter
    def name(self, value):
        """Raise error. Name setting is forbidden."""
        raise Exception("The Name of a park is immutable.")

    def park(self, car):
        """Park the car, if possible.

        Returns the coordinates of the space, or None if not successful.
        """
        raise Exception("Park.park method not implemented")

    def is_full():
        """Return the full status of the park instance."""
        raise Exception("Park.full method not implemented")

    def is_empty():
        """Return the empty status of the park instance."""
        raise Exception("Park.empty method not implemented")
