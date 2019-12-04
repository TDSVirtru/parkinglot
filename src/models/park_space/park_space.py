"""The park space model."""

from ..park import Park

from ..adjudicator import PREFERRED


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

    # Override the Park class park method.
    def park(self, car, preferred=False):
        """Park the car if possible.

        This ParkSpace.park method is the kernel of the process. It returns
        the coordinates of the space if the car parks, or none if it doesn't.
        """
        # Check to see if the space is already occupied
        if self.__car is not None:
            return None

        # get a sense of how good the match between car and space is
        match_result = self.adjudicator.match(car, self)

        # If the car and space are incompatible return None
        if match_result is None:
            return None

        # if the car is picky and the match not great, return None
        if preferred and match_result is not PREFERRED:
            return None

        # The space is compatible, and the car likes it well enough. Park it.
        self.__car = car
        return self.name

    # Override the Park method with this specialized test
    def is_full(self):
        """Return the full status of the park instance."""
        return self.__car is not None

    # Override the Park method with this specialized test
    def is_empty(self):
        """Return the empty status of the park instance."""
        return self.__car is None
