#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Eden Rusnell & Ming Fu'


def pig_latinify(word):
    output = ""
    vowels = "a, e, i, o, u"
    first_letter = word[0]
    # removed lowercase method
    # check if the first letter is a vowel
        # if the first letter is a vowel, add "yay
    if first_letter in vowels:
        new_word = word() + first_letter + "yay" # this doesn't make sense, as you haven't defined any of these variables
        new_word = new_word[1:] # this isn't the easiest way to do this
        print (new_word)
       # if the first letter is a consonant, more it to the end
        # keep moving letters to the end until the first letter is a vowel
        # add "ay" to the end of this new word
    # if a word begins with a vowel, append "yay" to the end of the word. for character in word:
    if first_letter not in vowels:
        word = word[1:] + word[0] + "ay"


    """
    Describe your function

    :param : one argument - a word
    :return: same word but in pig latin (either move 0 to end and add "ay", or, if "vowel", add "yay" to end
    :raises: ValueError (if word not a string), IndexError (if word is only one letter?)

    """

    return output









__license__ = "MIT License"
