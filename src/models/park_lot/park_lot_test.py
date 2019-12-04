"""Test model class ParkLot."""

import pytest  # noqa: F401

from .park_lot import ParkLot

from ..park_level import ParkLevel
from ..park_row import ParkRow
from ..park_space import ParkSpace
from ..car import Car


# @pytest.mark.skip()
def test_park_lot_construction_empty():
    foo = ParkLot("Fred")
    assert type(foo) is ParkLot
    assert foo.name == "Fred"
    assert len(foo.parks) == 0


# @pytest.mark.skip()
def test_park_lot_construct_with_levels():
    space111 = ParkSpace("S1")
    space112 = ParkSpace("S2")
    row11 = ParkRow("R1", [space111, space112])
    space121 = ParkSpace("S1")
    space122 = ParkSpace("S2")
    row12 = ParkRow("R2", [space121, space122])
    level1 = ParkLevel("L1", [row11, row12])
    space211 = ParkSpace("S1")
    space212 = ParkSpace("S2")
    row21 = ParkRow("R1", [space211, space212])
    space221 = ParkSpace("S1")
    space222 = ParkSpace("S2")
    row22 = ParkRow("R2", [space221, space222])
    level2 = ParkLevel("L1", [row21, row22])
    foo = ParkLot("P1", [level1, level2])
    assert type(foo) is ParkLot
    assert foo.name == "P1"
    assert len(foo.parks) == 2
    assert level1 in foo.parks
    assert level2 in foo.parks


# @pytest.mark.skip()
def test_park_lot_no_rows_status():
    """Check the degenerate case of no levels."""
    foo = ParkLot("Fred")
    assert foo.is_empty()
    assert foo.is_full()


# @pytest.mark.skip()
def test_park_level_fill_status():
    space111 = ParkSpace("S1")
    space112 = ParkSpace("S2")
    row11 = ParkRow("R1", [space111, space112])
    space121 = ParkSpace("S1")
    space122 = ParkSpace("S2")
    row12 = ParkRow("R2", [space121, space122])
    level1 = ParkLevel("L1", [row11, row12])
    space211 = ParkSpace("S1")
    space212 = ParkSpace("S2")
    row21 = ParkRow("R1", [space211, space212])
    space221 = ParkSpace("S1")
    space222 = ParkSpace("S2")
    row22 = ParkRow("R2", [space221, space222])
    level2 = ParkLevel("L1", [row21, row22])
    foo = ParkLot("P1", [level1, level2])
    assert foo.is_empty()
    assert not foo.is_full()
    foo.park(Car())
    assert not foo.is_empty()
    assert not foo.is_full()
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    assert not foo.is_empty()
    assert not foo.is_full()
    foo.park(Car())
    assert not foo.is_empty()
    assert foo.is_full()


# @pytest.mark.skip()
def test_park_row_reject_park_if_full():
    space111 = ParkSpace("S1")
    space112 = ParkSpace("S2")
    row11 = ParkRow("R1", [space111, space112])
    space121 = ParkSpace("S1")
    space122 = ParkSpace("S2")
    row12 = ParkRow("R2", [space121, space122])
    level1 = ParkLevel("L1", [row11, row12])
    space211 = ParkSpace("S1")
    space212 = ParkSpace("S2")
    row21 = ParkRow("R1", [space211, space212])
    space221 = ParkSpace("S1")
    space222 = ParkSpace("S2")
    row22 = ParkRow("R2", [space221, space222])
    level2 = ParkLevel("L1", [row21, row22])
    foo = ParkLot("P1", [level1, level2])
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    foo.park(Car())
    assert foo.is_full()
    assert foo.park(Car()) is None


# @pytest.mark.skip()
def test_park_row_check_return_address():
    space1 = ParkSpace("S1")
    row1 = ParkRow("R1", [space1])
    level1 = ParkLevel("L1", [row1])
    foo = ParkLevel("P1", [level1])
    assert foo.park(Car()) == "P1-L1-R1-S1"


# @pytest.mark.skip()
def test_park_lot_factory_method():
    foo = ParkLot.create({
        'name': "LotA",
        'levels': [
            {
                'name': "ground",
                'rows': [
                    {
                        'name': "r1",
                        'spaces': [
                            {'name': "01", 'attr': ["C"]},
                            {'name': "02", 'attr': ["C"]},
                        ]
                    },
                    {
                        'name': "r2",
                        'spaces': [
                            {'name': "04", 'attr': []},
                            {'name': "05", 'attr': []}
                        ]
                    }
                ]
            },
            {
                'name': "first",
                'rows': [
                    {
                        'name': "r1",
                        'spaces': [
                            {'name': "12", 'attr': ["H"]},
                            {'name': "13", 'attr': []},
                        ]
                    },
                    {
                        'name': "r2",
                        'spaces': [
                            {'name': "14", 'attr': ["E"]},
                            {'name': "15", 'attr': []}
                        ]
                    }
                ]
            }
        ]
    })
    assert foo.name == "LotA"
    assert len(foo.parks) == 2
    assert foo.is_empty()
    print(foo.park(Car.create({'attrs': ["E"]}), True))
    print(foo.park(Car.create({'attrs': []})))
    print(foo.park(Car.create({'attrs': []})))
    print(foo.park(Car.create({'attrs': ["H"]})))
    print(foo.park(Car.create({'attrs': []})))
    print(foo.park(Car.create({'attrs': []})))
    print(foo.park(Car.create({'attrs': ["C"]})))
    assert not foo.is_full()
    print(foo.park(Car.create({'attrs': ["C"]})))
    assert foo.is_full()
