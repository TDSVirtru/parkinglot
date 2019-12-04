"""Adjudicator model."""


from ..attribute import PREFERS
from ..attribute import REJECTS

ALLOWED = "allowed"
PREFERRED = "prefered"


class Adjudicator:
    """Adjudicator class."""

    def match(self, car, space):
        """Determine the match between this car and this space.

        The return values are - None, for not permitted; ALLOWED, for permitted
        but the car does not prefer the space; and PREFERRED, for when the car
        is both permitted to park there and prefers to park there.
        """
        # Check the space attributes to see if any want to block the car
        for attr in space.attributes:
            if attr.permits(car) is False:
                return None

        # If here then there the space will not block the car from parking.
        # Next, determine how much the car wants to park there
        for attr in car.attributes:
            if attr.desires(space) is PREFERS:
                return PREFERRED
            if attr.desires(space) is REJECTS:
                return None

        # All desires were ACCEPTS, so the space is acceptable:
        return ALLOWED
