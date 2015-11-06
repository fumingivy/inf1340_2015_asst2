#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find

THEME_SONG = "It's gonna get a little weird" \
             "gonna get a little wild" \
             "I ain't from round here" \
             "I'm from another dimension" \
             "gonna get a little weird" \
             "gonna have a good! time!" \
             "I ain't from round here" \
             "I'm from another WHOO-HOO" \
             "I'm talkin rainbows" \
             "I'm talking puppies" \
             "it's gonna get a little weird" \
             "gonna get a little wild" \
             "I ain't from round here" \
             "I'm from another dimension!"

def test_find_basic():

    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"



# test cases
# include instances where substring is found
# include instances where substring is not found
# does that refer to ones where the substring isn't present in the string?

def test_find_normal():
    assert find("I'm in class right now", "now", 0, 21) == 19
    assert find(THEME_SONG, "dimension", 0, 337) == 92


def test_multi_find_normal():
    assert multi_find(THEME_SONG, "weird", 0, 337) == "24,120,259"
    assert multi_find(THEME_SONG, "wild", 0, 337) == "48,283"

def test_not_found_find():
    assert find("I'm busy", "Jackson", 0, 7) == -1

def test_not_found_multi_find():
    assert multi_find(THEME_SONG, "Star Butterfly", 0, 337) == ""

def test_find_substring():
    assert find("I'm in class right now", "now", 0, 22) == 19

# include instances where substring is not found


def test_not_in_scope():
    assert find("I am starving now.", "now", 0, 8) == -1


def test_end_negative():
    assert find("Class is warmer than my home.", "my", 0, -29) == -1

def test_start_negative():
    assert find("We need coffee.", "coffee", -1, -15) == -1

