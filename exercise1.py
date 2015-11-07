#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Eden Rusnell & Ming Fu'

"""
assumptions:
that the word is going to be English
that the letter y is always a consonant (eg. "xylophone" is "olophonexylay" not "ylophonexay")
"""


# function to return word in pig latin
def pig_latinify(word):
    output = ""
    vowels = "aeiou, AEIOU"
    word = str(word)
    if word.isdigit():
        raise ValueError
    if word[0] in vowels:
        return word + "yay"
    for letter in word:
        word = word[1:] + word[0]
        if word[0] in vowels:
            return word + "ay"
    if vowels not in word:
        return word[1:] + word[0] + "ay"





# print pig_latinify("word")
print pig_latinify("xylophone")