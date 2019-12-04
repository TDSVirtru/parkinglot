"""internal service for parking lots."""

from ..models import ParkLot


class ParkingService:
    """Parking lot service."""

    def __init__(self, opts):
        """Construct a parking lot service."""
        self._lot = ParkLot.create(opts)

    def park(self, car):
        """Park the car"""
        # Try to park the car in a preferred spot
        spot = self._lot.park(car, True)

        # if that fails try in any legal spot
        if spot is None:
            spot = self._lot.park(car, False)

        if spot is not None:
            print("Car {0} was parked in {1}".format(car.name, spot))
        else:
            print("Car {0} could not be parked".format(car.name))

        print("Lot is full? {}".format(self._lot.is_full()))
        print("")
