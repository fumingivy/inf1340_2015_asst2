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


# tests for when the letter y is a vowel instead of a consonant
def test_y_is_vowel():
     assert pig_latinify("why") == "ywhay"
     assert pig_latinify("cry") == "ycray"
     assert pig_latinify("xylophone") == "ylophonexay"

# tests for when the letter y is a consonant
def test_y_is_consonant():
    assert pig_latinify("yellow") == "ellowyay"
    assert pig_latinify("young") == "oungyay"
    assert pig_latinify("Yankees") == "ankeesYay"

# tests for words that start with q (to see if "qu" exception works)
def test_starts_with_q():
    assert pig_latinify("question") == "estionquay"
    assert pig_latinify("queen") == "eenquay"
    assert pig_latinify("quietly") == "ietlyquay"

# tests for words with capital letters in them
def test_with_capital():
     assert pig_latinify("Canada") == "anadaCay"
     assert pig_latinify("TORONTO") == "ORONTOTay"

# tests for different kind of errors
def test_for_errors():
    try:
        pig_latinify(12345)
    except TypeError:
        assert pig_latinify(12345) == TypeError
    assert pig_latinify("hyphenated-word") == ""
    assert pig_latinify(12345) == ""
    assert pig_latinify("username1withnumbers") == ""


