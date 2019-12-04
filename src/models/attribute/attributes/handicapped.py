"""The Handicapped attribute model."""

from ..attribute import Attribute

from ..attribute import PREFERS
from ..attribute import REJECTS

HANDICAPPED = "Handicapped"


class Handicapped(Attribute):
    """Handicapped class."""

    def __init__(self):
        """Construct a handicapped."""
        Attribute.__init__(self, HANDICAPPED)

    def permits(self, car):
        """Determine if car contains attribute Handicapped."""
        if self in car.attributes:
            return True
        return False

    def desires(self, space):
        """Determine how much this handicapped Car desires the space."""
        if self in space.attributes:
            return PREFERS
        return REJECTS
