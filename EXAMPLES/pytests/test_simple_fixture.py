#!/usr/bin/env python
from collections import namedtuple
import pytest
from person import Person

FIRST_NAME = "Guido"
LAST_NAME = "Von Rossum"

@pytest.fixture  # <2>
def person():
    """
    Return a 'Person' named tuple with fields 'first_name' and 'last_name'
    """
    p = Person(FIRST_NAME, LAST_NAME)
    return p  # <3>

@pytest.fixture
def the_answer():
    return 42

def test_first_name(person, the_answer):  # <4>
    assert person.first_name == FIRST_NAME
    assert the_answer == 42

def test_last_name(person):  # <4>
    assert person.last_name == LAST_NAME

