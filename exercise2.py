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
    for character in range(start, end):
        if substring[0] == input_string[index]:
            return index
        index += 1
    # take the input string as input_string[start:end]
    # search the input string character by character for the substring
        # this requires the use of a for loop
    # return the index where the substring starts
    # if substring isn't there, return NONE (or -1?)
    """
    Describe your function

    :param : takes as argument the string, the substring that is being searched for, the start and the end
    :return: returns the "lowest index (integer) where the substring is found in the index range start <= index <= end"
    :raises: ValueError (not entering a string)

    """


def multi_find(input_string, substring, start, end):
    index = 0
    while index <= end:
        for character in range(start, end):
            if substring[0] == input_string[index]:
                return index
            index += 1

    # search the input string character by character for the substring
        # do this for each letter PAST the start of the first instance of the substring
        # this requires a while-loop
        # condition that controls while look is an index count?
    # return EACH index where the substring starts
    # if the substring isn't there, return NONE (or -1?)
    """
    Describe your function

    :param : a string, a substring, a start index, and an end index
    :return: a string with zero or more indices separated by commas
    :raises: ValueError

    """
    result = ""

    return result

print find("hello", "el", 0, 4)
print multi_find("hello hello hello", "el", 0, 14)