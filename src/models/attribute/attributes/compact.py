"""The Compact attribute."""

from ..attribute import Attribute

from ..attribute import ACCEPTS

COMPACT = "Compact"


class Compact(Attribute):
    """Compact attribute class."""

    def __init__(self):
        """Construct a Compact."""
        Attribute.__init__(self, COMPACT)

    def permits(self, car):
        """Determine if car includes attribute Compact."""
        if self in car.attributes:
            return True
        return False

    def desires(self, space):
        """Return ACCEPTS for every kind of space."""
        return ACCEPTS
