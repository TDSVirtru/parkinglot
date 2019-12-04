"""Attribute model."""

PREFERS = "prefers"
ACCEPTS = "accepts"
REJECTS = "rejects"


class Attribute:
    """The abstract Attribute class."""

    def __init__(self, name=None):
        """Construct a Attribute with a value string."""
        self.__name = name
        self.__hash = hash(name)

    def __hash__(self):
        return self.__hash

    def __eq__(self, other):
        return self.attribute == other.attribute

    @property
    def attribute(self):
        """Return the attribute name."""
        return self.__name

    @attribute.setter
    def attribute(self, value):
        """NOOP the request to protect the internal name value."""
        pass

    def permits(self, car):
        """Determine if a Space attribute permits the car to park.

        Acceptable responses are the boolean values True and False.
        """
        raise Exception("Abstract method Attribute.permits() not defined")

    def desires(self, space):
        """Determine how much a Car attribute desires a space.

        Acceptable responses are PREFERS, ACCEPTS, and REJECTS."""
        raise Exception("Abstract method Attribute.desires() not defined")
