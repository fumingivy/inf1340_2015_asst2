#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


"""
add your own test cases to test_exercise1

be sure to use a variety of initial letters
"""

def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"


def test_first_letter_vowel():
     assert pig_latinify("abroad") == "abroadyay"

def test_first_letter_consonant():
     assert pig_latinify("pie") == "iepay"

def test_first_letter_consonant():
     assert pig_latinify(" ") == "None"