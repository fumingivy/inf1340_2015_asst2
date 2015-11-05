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
    assert pig_latinify("agoraphobic") == "agoraphobicyay"
    assert pig_latinify("bumblebee") == "umblebeebay"
    assert pig_latinify("crashing") == "ashingcray"
    assert pig_latinify("divinity") == "ivinityday"
    assert pig_latinify("ergonomic") == "ergonomicyay"
    assert pig_latinify("fortunate") == "ortunatefay"
    assert pig_latinify("goulash") == "oulashgay"
    assert pig_latinify("herbs") == "erbshay"
    assert pig_latinify("igloo") == "iglooyay"
    assert pig_latinify("jealousy") == "ealousyjay"
    assert pig_latinify("killers") == "illerskay"
    assert pig_latinify("linework") == "ineworklay"
    assert pig_latinify("manageable") == "anageablemay"
    assert pig_latinify("noble") == "oblenay"
    assert pig_latinify("opulent") == "opulentyay"
    assert pig_latinify("quietly") == "ietlyquay"
    assert pig_latinify("robust") == "obustray"
    assert pig_latinify("sombulent") == "ombulentsay"
    assert pig_latinify("television") == "elevisiontay"
    assert pig_latinify("university") == "universityyay"
    assert pig_latinify("witchy") == "itchyway"
    assert pig_latinify("xylophone") == "ylophonexay"
    assert pig_latinify("yellow") == "ellowyay"
    assert pig_latinify("zed") == "edzay"




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