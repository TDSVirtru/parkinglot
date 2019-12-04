"""Car model."""

from ..attribute import Compact
from ..attribute import Electric
from ..attribute import Handicapped


class Car:
    """Car class."""

    @classmethod
    def create(cls, opts):
        """Unpack serialization object and return an ParkRow."""
        attrs = []
        if "attrs" in opts:
            for attr in opts['attrs']:
                if attr == "H":
                    attrs.append(Handicapped())
                if attr == "C":
                    attrs.append(Compact())
                if attr == "E":
                    attrs.append(Electric())
        name = ""
        if "name" in opts:
            name = opts['name']

        return cls(attrs, name)

    def __init__(self, attributes=None,  name=""):
        """Construct a car."""
        # TODO - check to see if attributes are a list of Attributes
        # TODO - assign a unique id for unpark operations
        self.__attr_set = set() if attributes is None else set(attributes)
        self.__name = name

    @property
    def name(self):
        """Return the name of the car."""
        return self.__name

    @name.setter
    def name(self, value):
        """Raise an exception if atttempt is made to set name."""
        raise Exception("cannot set new name for a car")

    @property
    def attributes(self):
        """Return the set of attributes for this car."""
        return self.__attr_set.copy()  # do not hand out the master set

    @attributes.setter
    def attributes(self, value):
        """Raise an exception if atttempt is made to set attributes."""
        raise Exception("cannot set attributes on a car")
