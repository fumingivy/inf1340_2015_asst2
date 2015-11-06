#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Eden Rusnell & Ming Fu'



# function to return word in pig latin
def pig_latinify(word):
    output = ""
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "yay"
    if word[0] == ("q" or "Q"):
        if word[1] == ("u" or "U"):
            return word[2:] + word[0:2] + "ay"
    while word[0] not in vowels:
        word = word[1:] + word[0]
        if word[0] in vowels:
            return word + "ay"
        if word[0] is ("y" or "Y"):
            return word + "ay"

#pig_latinify("word")