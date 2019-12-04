"""Test model class Adjudicator."""

import pytest  # noqa: F401

from .adjudicator import Adjudicator

from .adjudicator import ALLOWED
from .adjudicator import PREFERRED

from ..attribute import Compact
from ..attribute import Electric
from ..attribute import Handicapped

from ..car import Car
from ..park_space import ParkSpace


# @pytest.mark.skip()
def test_adjudicator_construction():
    assert type(Adjudicator()) is Adjudicator


# @pytest.mark.skip()
def test_adjudicator_no_attributes():
    car = Car([])
    space = ParkSpace("regular", [])
    adj = Adjudicator()
    assert adj.match(car, space) is ALLOWED


# @pytest.mark.skip()
def test_adjudicator_allowed_but_not_preffered():
    car = Car([Compact()])
    space = ParkSpace("regular", [])
    adj = Adjudicator()
    assert adj.match(car, space) is ALLOWED


# @pytest.mark.skip()
def test_adjudicator_space_rejects():
    car = Car([Compact()])
    space = ParkSpace("handicapped", [Handicapped()])
    adj = Adjudicator()
    assert adj.match(car, space) is None


# @pytest.mark.skip()
def test_adjudicator_car_rejects():
    car = Car([Handicapped()])
    space = ParkSpace("regular", [])
    adj = Adjudicator()
    assert adj.match(car, space) is None


# @pytest.mark.skip()
def test_adjudicator_car_prefers():
    car = Car([Electric()])
    space = ParkSpace("electric", [Electric()])
    adj = Adjudicator()
    assert adj.match(car, space) is PREFERRED
