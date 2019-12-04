"""The Handicapped attribute model."""

from ..attribute import Attribute

from ..attribute import PREFERS
from ..attribute import ACCEPTS
from ..attribute import REJECTS

HANDICAPPED = "Handicapped"


class Handicapped(Attribute):
    """Handicapped class."""

    def __init__(self):
        """Construct a handicapped."""
        Attribute.__init__(self, HANDICAPPED)

    def permits(self, Car):
        """Determine if Space attribute compact permits this car to park."""
        return False

    def desires(self, Space):
        """Determine how much this compact Car desires the space."""
        return ACCEPTS
