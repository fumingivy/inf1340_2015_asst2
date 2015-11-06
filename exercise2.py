#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Eden Rusnell & Ming Fu'

# function to find a single instance of a substring
def find(input_string, substring, start, end):
    index = 0
    for letter in range(start, end):
        if input_string[index:index+len(substring)] == substring:
            return index
        index += 1

    else:
        return "-1"


# function to find multiple instances of a substring
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




# find("hello", "el", 0, 5)
# multi_find("hello hello hello", "el", 0, 18)
