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

# tests for when the word is all vowels
def test__all_vowel():
     assert pig_latinify("eau") == "eauyay"
     assert pig_latinify("i.e.") == "i.e.yay"

# tests for when the letter y is a vowel instead of a consonant
def test_y_is_vowel():
     assert pig_latinify("why") == "ywhay"
     assert pig_latinify("cry") == "ycray"
     assert pig_latinify("xylophone") == "ylophonexay"

def test_y_is_consonant():
    assert pig_latinify("yellow") == "ellowyay"
    assert pig_latinify("young") == "oungyay"
    assert pig_latinify("Yankees") == "ankeesYay"

def test_starts_with_q():
    assert pig_latinify("question") == "estionquay"
    assert pig_latinify("queen") == "eenquay"
    assert pig_latinify("quietly") == "ietlyquay"

def test_with_numbers():
    assert pig_latinify("name123") == "ame123nay"
    assert pig_latinify("21st-century") == "entury21st-cay"

def test_with_capital():
     assert pig_latinify("Canada") == "anadaCay"
     assert pig_latinify("TORONTO") == "ORONTOTay"

def test_with_punctuation():
     assert pig_latinify("top-down") == "op-downtay"
     assert pig_latinify("X-eye") == "eyeX-ay"
     assert pig_latinify("e.g.") == "e.g.yay"
     assert pig_latinify("Capt.") == "apt.Cay"
     assert pig_latinify("ham-fisted") == "am-fistedhay"

def test_for_errors():
    try:
        pig_latinify(12345)
    except TypeError:
        assert True


