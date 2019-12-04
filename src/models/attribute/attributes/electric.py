"""The Electric attribute."""

from ..attribute import Attribute

from ..attribute import PREFERS
from ..attribute import ACCEPTS

ELECTRIC = "Electric"


class Electric(Attribute):
    """Electric class."""

    def __init__(self):
        """Construct an Electric."""
        Attribute.__init__(self, ELECTRIC)

    def permits(self, car):
        """Determine if car contains attribute Electric."""
        if self in car.attributes:
            return True
        return False

    def desires(self, space):
        """Determine how much this electric Car desires the space."""
        if self in space.attributes:
            print('ping')
            return PREFERS
        return ACCEPTS
