"""Test model class Attribute."""

import pytest  # noqa: F401

from .attribute import Attribute


# @pytest.mark.skip()
def test_attribute_construction_empty():
    foo = Attribute()
    assert type(foo) is Attribute
    assert foo.attribute is None


def test_attribute_construction_with_name():
    foo = Attribute("FOO")
    assert type(foo) is Attribute
    assert foo.attribute == "FOO"


def test_attribute_name_durability():
    foo = Attribute("FOO")
    foo.attribute = "BAR"
    assert foo.attribute == "FOO"


def test_attribute_relative_equal():
    foo = Attribute("This is an attribute")
    bar = Attribute("This is an attribute")
    assert foo == bar
    assert foo.__hash__() == bar.__hash__()


def test_attribute_abstraction_for_permits():
    foo = Attribute()
    with pytest.raises(Exception):
        foo.permits(None)


def test_attribute_abstraction_for_desires():
    foo = Attribute()
    with pytest.raises(Exception):
        foo.desires(None)
