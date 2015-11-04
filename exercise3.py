#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def union(table1, table2):
    row = 0
    index = 0
    # compares the tables row by row to make sure that each entry (i.e. table[row][column]) matches.
    # takes one version of the rows that match
    # takes from both tables the rows that done match
    # returns a new table of all the rows that appear in table1 or table2 or both
        #remove duplicates
        # possible to not generate duplicates in the first place
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    return []


def intersection(table1, table2):
    row = 0
    index = 0
    # does row-by-row comparison of tables
    # does index-by-index comparison of rows
    # finds rows that are in both table1 and table2
    # creates a new table containing those rows
    """
    Describe your function
    1. checks that the schema for both tables are the same
    2. returns a new table that contains all unique rows that appear in BOTH tables
    :raises: MismathedAttributesException Error
    """
    return []


def difference(table1, table2):
    row = 0
    index = 0
    """
    Describe your function
    1. checks that the schema for both tables are the same
    2. returns a new table that contains all unique rows that appear in the FIRST table but not the second
    :raises: MismatchedAttributesException Error
    """
    return []


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

