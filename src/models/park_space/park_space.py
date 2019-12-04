"""The park space model."""

from ..park import Park


class ParkSpace(Park):
    """Park space class."""

    def __init__(self, name, attributes=None):
        """Construct a park space."""
        Park.__init__(self, name)
        # TODO - check to see if attributes are a list of Attributes
        self.__attr_set = set() if attributes is None else set(attributes)
        self.__car = None

    @property
    def attributes(self):
        """Return the set of attributes for this park space."""
        return self.__attr_set.copy()  # do not hand out the master set

    @attributes.setter
    def attributes(self, value):
        """Raise an exception if atttempt is made to set attributes."""
        raise Exception("cannot set attributes on a park space")

    @property
    def car(self):
        """Return the car parked in this space, if any."""
        return self.__car  # do not hand out the master set

    @car.setter
    def car(self, value):
        """Raise an exception if atttempt is made to set the value of car."""
        raise Exception("cannot alter the value of car on a park space")

    def park(self, car):
        """Park the car if possible.

        Returns the coordinates of the space if successful, or None if
        the space is full or the car doesn't have the attributes required.
        """
        # Check to see if the space is already occupied
        if self.__car is not None:
            return None

        # TODO - check with the adudicator to see if this is possible

        # Park the car
        self.__car = car
        return self.name

    def is_full(self):
        """Return the full status of the park instance."""
        return self.__car is not None

    def is_empty(self):
        """Return the empty status of the park instance."""
        return self.__car is None
