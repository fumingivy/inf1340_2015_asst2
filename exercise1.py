#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """

    word = raw_input("Please type your word: "):

# set two appendix as variables
    var1 = "yay"
    var2 = "ay"


# make sure the word format
    if len(word) > 0 and word.isalpha():
        word_lowercase = word.lower()
        first_letter = word_lowercase [0]


# if a word begins with a vowel, append "yay" to the end of the word.
        if first_letter = "a" or "e" or "i" or "o" or "u":
            new_word = word_lowercase + first_letter + var1
            new_word = new_word [1:]
            print (new_word)
