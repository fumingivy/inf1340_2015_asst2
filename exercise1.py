#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Eden Rusnell & Ming Fu'

"""
assumptions:
that the word is going to be English
that the word is not going to include punctuation
explanation for "qu" exception: English-speakers find it hard to understand q with a vowel other than u following it,
we decided to have the pig_latinify function move "qu" to the end instead of just "q" (which returns the result
"eryquay" instead of "ueryqay" for "query"). If that was undersirable, it would be simple enough to remove the exception.
"""


# function to return word in pig latin
def pig_latinify(word):
    output = ""
    vowels = "aeiou, AEIOU"
    word = str(word)
    if word.isalpha():
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
    else:
        return ""


#pig_latinify("word")