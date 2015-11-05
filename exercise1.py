#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Eden Rusnell & Ming Fu'


# assuming word is lowercase, and is changeable
def pig_latinify(word):
    output = ""
    vowels = "aeiou"
    y_except = "y"
    first_letter = word[0]
    if first_letter in vowels:
        return word + "yay"
    if first_letter == "q":
        if word[1] == "u":
            return word[2:] + word[0:2] + "ay"
    while first_letter not in vowels:
        word = word[1:] + word[0]
        first_letter = word[0]
        if first_letter in vowels:
            return word + "ay"
        if first_letter in y_except:
            return word + "ay"


__license__ = "MIT License"
