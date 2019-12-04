"""Main program."""

import json
import sys

from pprint import pprint

from src.services import ParkingService

from src.models import Car


def main():
    args = sys.argv[1:]

    path = "cases/case1.json" if len(args) == 0 else args[0]

    print("")
    print("Reading case file from path={}".format(path))
    print("")

    case = {}
    with open(path, 'r') as f:
        case = json.load(f)

    pprint(case)

    service = ParkingService(case['parking_lot'])

    for car in case['cars']:
        service.park(Car.create(car))


if __name__ == "__main__":
    main()
