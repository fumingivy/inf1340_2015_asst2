#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

def find(input_string, substring, start, end):
    index = 0
    for letter in range(start, end):
        if input_string[index:index+len(substring)] == substring:
            return index
        index += 1

    else:
        return "-1"


    # if substring isn't there, return NONE (or -1?)

THEME_SONG = "It's gonna get a little weird" \
             "gonna get a little wild" \
             "I ain't from round here" \
             "I'm from another dimension" \
             "gonna get a little weird" \
             "gonna have a good! time!" \
             "I ain't from round here" \
             "I'm from another WHOO-HOO" \
             "I'm talkin rainbows" \
             "I'm talking puppies" \
             "it's gonna get a little weird" \
             "gonna get a little wild" \
             "I ain't from round here" \
             "I'm from another dimension!"

def multi_find(input_string, substring, start, end):
    index = 0
    indexes = ""
    while index < end:
        for letter in range(start, end):
            if input_string[index:index+len(substring)] == substring:
                indexes += str(index) + ","
            index += 1
        indexes = indexes[0:-1]
        return indexes
    else:
        return " "


    # if the substring isn't there, return NONE (or -1?)


print find("hello", "el", 0, 5)
print multi_find("hello hello hello", "el", 0, 18)
