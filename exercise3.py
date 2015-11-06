#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Eden Rusnell & Ming Fu'


MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

GRADUATES = [["Number", "Surname", "Age"],
            [7274, "Robinson", 37],
            [9824, "Darkes", 38],
            [7432, "O'Malley", 39]]

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
        return False

def union(table1, table2):
    row = 0
    new_table = []
    for line in table1:
        new_table += [table1[row]]
        new_table += [table2[row]]
        row += 1
    new_table = remove_duplicates(new_table)
    return new_table

def intersection(table1, table2):
    row = 0
    row1 = 1
    new_table = [table1[0]]
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


def difference(table1, table2):
    row = 0
    row1 = 0
    new_table = [table1[0]]
    unique = False
    for rows in table1[0:-1]:
        index = 0
        for columns in table1[row1]:
            if table1[row1][index] == table2[row][index]:
                unique = False
            else:
                unique = True
            index += 1
        if unique is True:
            new_table += [table1[row1]]
        row += 1
    row1 += 1
    return new_table

# print union(GRADUATES, MANAGERS)
# print difference(GRADUATES, MANAGERS)
# print difference(MANAGERS, GRADUATES)
# print intersection(GRADUATES, MANAGERS)


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

