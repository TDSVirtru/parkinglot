"""Car model."""


class Car:
    """Car class."""

    def __init__(self, attributes=None):
        """Construct a car."""
        # TODO - check to see if attributes are a list of Attributes
        # TODO - assign a unique id for unpark operations
        self.__attr_set = set() if attributes is None else set(attributes)

    @property
    def attributes(self):
        """Return the set of attributes for this car."""
        return self.__attr_set.copy()  # do not hand out the master set

    @attributes.setter
    def attributes(self, value):
        """Raise an exception if atttempt is made to set attributes."""
        raise Exception("cannot set attributes on a car")
