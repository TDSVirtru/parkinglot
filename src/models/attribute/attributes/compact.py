"""The Compact attribute."""

from ..attribute import Attribute

from ..attribute import PREFERS
from ..attribute import ACCEPTS
from ..attribute import REJECTS

COMPACT = "Compact"


class Compact(Attribute):
    """Compact attribute class."""

    def __init__(self):
        """Construct a Compact."""
        Attribute.__init__(self, COMPACT)

    def permits(self, Car):
        """Determine if Space attribute compact permits this car to park."""
        return False

    def desires(self, Space):
        """Determine how much this compact Car desires the space."""
        return ACCEPTS
