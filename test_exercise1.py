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
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

def test_alphabet():
    assert pig_latinify("agoraphobic")
    assert pig_latinify("bumblebee")
    assert pig_latinify("crasching")
    assert pig_latinify("divinity")
    assert pig_latinify("ergonomic")
    assert pig_latinify("fortunate")
    assert pig_latinify("goulash")
    assert pig_latinify("herbs")
    assert pig_latinify("igloo")
    assert pig_latinify("jealousy")
    assert pig_latinify("killers")
    assert pig_latinify("linework")
    assert pig_latinify("manageable")
    assert pig_latinify("noble")
    assert pig_latinify("opulent")
    assert pig_latinify("quietly")
    assert pig_latinify("robust")
    assert pig_latinify("sombulent")
    assert pig_latinify("television")
    assert pig_latinify("university")
    assert pig_latinify("witchy")
    assert pig_latinify("xylophone")
    assert pig_latinify("yellow")
    assert pig_latinify("zed")




def test_first_letter_vowel():
     assert pig_latinify("abroad") == "abroadyay"

def test__not_first_letter_vowel():
     assert pig_latinify("pie") == "iepay"

def test__all_vowel():
     assert pig_latinify("eye") == "eyeyay"

def test_with_numbers():
     assert pig_latinify("name123") == "ame123nay"

def test_with_hyphen():
     assert pig_latinify("top-down") == "op-downtay"


# add exception for when y is a vowel