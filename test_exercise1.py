#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Eden Rusnell & Ming Fu'


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

# tests for when the first letter is a vowel
def test_first_letter_vowel():
     assert pig_latinify("abroad") == "abroadyay"
     assert pig_latinify("eligible") == "eligibleyay"
     assert pig_latinify("ideal") == "idealyay"
     assert pig_latinify("oil") == "oilyay"
     assert pig_latinify("utility") == "utilityyay"

# tests for when the first letter is a consonant
def test_first_letter_consonant():
     assert pig_latinify("banana") == "ananabay"
     assert pig_latinify("cream") == "eamcray"
     assert pig_latinify("do") == "oday"
     assert pig_latinify("fantastic") == "antasticfay"
     assert pig_latinify("pie") == "iepay"

# tests for when the word is all vowels
def test__all_vowel():
     assert pig_latinify("eau") == "eauyay"
     assert pig_latinify("i.e.") == "i.e.yay"

# tests for when the letter y is a vowel instead of a consonant
def test__all_consonant():
     assert pig_latinify("why") == "ywhay"
     assert pig_latinify("cry") == "ycray"


def test_with_numbers():
    assert pig_latinify("name123") == "ame123nay"
    assert pig_latinify("21st-century") == "entury21st-cay"

def test_with_capital():
     assert pig_latinify("Canada") == "anadaCay"
     assert pig_latinify("TORONTO") == "ORONTOTay"

def test_with_hyphen():
     assert pig_latinify("top-down") == "op-downtay"
     assert pig_latinify("X-eye") == "eyeX-ay"

def test_with_dot():
     assert pig_latinify("e.g.") == "e.g.yay"
     assert pig_latinify("Capt.") == "apt.Cay"


# add exception for when y is a vowel