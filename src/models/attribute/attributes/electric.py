"""The Electric attribute."""

from ..attribute import Attribute

from ..attribute import PREFERS
from ..attribute import ACCEPTS
from ..attribute import REJECTS

ELECTRIC = "Electric"


class Electric(Attribute):
    """Electric class."""

    def __init__(self):
        """Construct an Electric."""
        Attribute.__init__(self, ELECTRIC)

    def permits(self, Car):
        """Determine if Space attribute electric permits this car to park."""
        return False

    def desires(self, Space):
        """Determine how much this electric Car desires the space."""
        return ACCEPTS
