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

def test__not_first_letter_vowel():
     assert pig_latinify("pie") == "iepay"

def test_multi_vowel():
     assert pig_latinify("computer") == "omputercay"

def test__all_vowel():
     assert pig_latinify("eau") == "eauyay"

def test__only_consonants():
     assert pig_latinify("why") == "whyay"

def test_with_numbers():
     assert pig_latinify("name123") == "ame123nay"

def test_with_hyphen():
     assert pig_latinify("top-down") == "op-downtay"

def test_with_dot():
     assert pig_latinify("i.e.") == "i.e.yay"

# add exception for when y is a vowel