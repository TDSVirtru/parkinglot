"""internal service for park level."""

from ..park import Park
from ..park_row import ParkRow


class ParkLevel(Park):
    """Park level class."""

    @classmethod
    def create(cls, opts):
        """Unpack serialization object and return an ParkRow."""
        rows = []
        if "rows" in opts:
            for row in opts['rows']:
                rows.append(ParkRow.create(row))

        return cls(opts['name'], rows)

    def __init__(self, name, rows=[]):
        """Construct a ParkLevel."""
        Park.__init__(self, name, rows)
