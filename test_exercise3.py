#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Eden Rusnell & Ming Fu'

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

MISMATCHED = [["Name", "Age", "Title", "Sign"],
              ["Tom", 23, "Dr.", "Libra"],
              ["Jenny", 47, "Captain", "Gemini"]]

#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
     return sorted(t1) == sorted(t2)

###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

# test cases added by module authors


def test_intersection_works():
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]
    assert is_equal(result, intersection(MANAGERS, GRADUATES))


def test_intersection_errors():
    assert intersection(GRADUATES, MISMATCHED) is None
    assert intersection(MANAGERS, MISMATCHED) is None

def test_difference_works():
    result = [["Number", "Surname", "Age"],
              [9297, "O'Malley", 56]]
    assert is_equal(result, difference(MANAGERS, GRADUATES))

    result2 = [["Number", "Surname", "Age"],
               [7274, "Robinson", 37]]
    assert is_equal(result2, difference(GRADUATES, MANAGERS))

def test_difference_errors():
    assert difference(GRADUATES, MISMATCHED) is None
    assert difference(MANAGERS, MISMATCHED) is None

def test_union_works():
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]
    assert is_equal(result, union(MANAGERS, GRADUATES))

def test_union_errors():
    assert union(GRADUATES, MISMATCHED) is None
    assert union(MANAGERS, MISMATCHED) is None

def test_error_raised():
    try:
        union(MANAGERS, MISMATCHED)
    except MismatchedAttributesException:
        assert True

