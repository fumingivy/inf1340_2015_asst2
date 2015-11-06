#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Eden Rusnell & Ming Fu'

"""
Assumptions:
1. that when rows are indentical they do not have spelling errors or typos
2. that all tables have their contents in the same order
"""
##########
# TABLES #
##########


GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

MISMATCHED = [["Name", "Age", "Title", "Sign"],
              ["Tom", 23, "Dr.", "Libra"],
              ["Jenny", 47, "Captain", "Gemini"]]

TIMS_LIST = [["Name", "Quest", "Colour"],
            ["Arthur", "To seek the Grail", "Blue"],
            ["Robin", "To seek the Grail," "Blue - no, yellow!"]]

TIMS_ASKS = [["Name", "Quest", "Colour"],
            ["Arthur", "To seek the Grail", "Blue"],
            ["Galahad", "To seek the Grail", "Red"],
            ["Lancelot", "To seek the Grail", "Mauve"],
            ["Ringo", "To seek the Grail", "Turquoise"],
            ["Arthur", "To seek the Grail", "Blue"]]

#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


#############
# FUNCTIONS##
############


# function to check that schemas match
def check_match(table1, table2):
    index = 0
    matching = False
    for column in table1[0]:
        if table1[0][index] == table2[0][index]:
            matching = True
            index += 1
        else:
            matching = False
    if matching is True:
        return True
    else:
        MismatchedAttributesException
        return ""


# function to return a new table that contains all rows that appear in either table
def union(table1, table2):
    matching = check_match(table1, table2)
    if matching is True:
        new_table = []
        new_table += table1
        new_table += table2
        new_table = remove_duplicates(new_table)
        return new_table


# function to return a new table that contains all rows that appear in both tables
def intersection(table1, table2):
    matching = check_match(table1, table2)
    if matching is True:
        row = 0
        row1 = 0
        new_table = []
        in_both = False
        while row1 < len(table1):
            row = 0
            for rows in table1:
                index = 0
                for columns in table1[row1]:
                    if table1[row1][index] == table2[row][index]:
                        in_both = True
                    else:
                        in_both = False
                    index += 1
                if in_both is True:
                    new_table += [table1[row1]]
                row += 1
            row1 += 1
        return new_table


# function to return a table that contains (table header and) all rows that appear in the first table only
def difference(table1, table2):
    matching = check_match(table1, table2)
    if matching is True:
        row = 0
        new_table = [table1[0]]
        unique = False
        for rows in table1:
            index = 0
            for columns in table1[row]:
                if table1[row][index] == table2[row][index]:
                    unique = False
                else:
                    unique = True
                index += 1
                if unique is True:
                    new_table += [table1[row]]
            row += 1
        new_table = remove_duplicates(new_table)
        return new_table

