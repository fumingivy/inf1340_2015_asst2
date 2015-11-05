#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


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

def test_find_substring():
    assert find("I'm in class right now", "now", 0, 22) == 19

# include instances where substring is not found

def test_not_find_substring():
    assert find("I'm in class right now", "signal", 0, 22) == -1

def test_not_in_scope():
    assert find("I'm in class right now", "signal", 0, 15) == -1

def test_scope_is_large():
    assert find("I'm in class right now", "signal", 0, 25) == -1

def test_end_negative():
    assert find("I'm in class right now", "signal", 0, -22) == -1

def test_start_():
    assert find("I'm in class right now", "signal", -1, -22) == -1

def test_find_specific():
    assert find("I'm in class right now", "signal", -22, -1) == -1

