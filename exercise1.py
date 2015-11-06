#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Eden Rusnell & Ming Fu'



# function to return word in pig latin
def pig_latinify(word):
    output = ""
    vowels = "aeiouAEIOU"
    first_letter = word[0]
    if first_letter in vowels:
        return word + "yay"
    if first_letter == ("q" or "Q"):
        if word[1] == ("u" or "U"):
            return word[2:] + word[0:2] + "ay"
    while first_letter not in vowels:
        word = word[1:] + word[0]
        first_letter = word[0]
        if first_letter in vowels:
            return word + "ay"
        if first_letter is ("y" or "Y"):
            return word + "ay"

#pig_latinify("word")