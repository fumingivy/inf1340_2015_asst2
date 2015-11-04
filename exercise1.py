#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"



def pig_latinify(word):
    output = ""
    vowels = "aeiou"

    """
    Describe your function

    :param : one argument - a word
    :return: same word but in pig latin (either move 0 to end and add "ay", or, if "vowel", add "yay" to end
    :raises: ValueError (if word not a string), IndexError (if word is only one letter?)

    """
    #first step: convert to lowercase?
    #second: search the word at index 0 to figure out if the word beings with a vowel or a consonant
        #third (if-consonant): move index 0 letter to the end
    #fourth: append either "ay" or "yay"
    return output


# set two appendix as variables
var1 = "yay"
var2 = "ay"


# make sure the word format
if len(word) > 0 and word.isalpha():
    word_lowercase = word.lower()
    first_letter = word_lowercase [0]


# if a word begins with a vowel, append "yay" to the end of the word.
if first_letter == "a" or "e" or "i" or "o" or "u":
    new_word = word.lowercase() + first_letter + var1 # this doesn't make sense, as you haven't defined any of these variables
    new_word = new_word [1:]
    print (new_word)


__license__ = "MIT License"
