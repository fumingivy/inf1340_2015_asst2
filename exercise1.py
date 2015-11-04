#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Eden Rusnell & Ming Fu'


def pig_latinify(word):
    output = ""
    vowels = "aeiou"
    first_letter = word[0]
    # removed lowercase method
    if first_letter in vowels:
        return word + "yay"
    while first_letter not in vowels:
        word = word[1:] + word[0]
        first_letter = word[0]
        if first_letter in vowels:
            return word + "ay"


    """
    Describe your function

    :param : one argument - a word
    :return: same word but in pig latin (either move 0 to end and add "ay", or, if "vowel", add "yay" to end
    :raises: ValueError (if word not a string), IndexError (if word is only one letter?)

    """

print pig_latinify("pear")
print pig_latinify("apple")
print pig_latinify("scratch")







__license__ = "MIT License"
