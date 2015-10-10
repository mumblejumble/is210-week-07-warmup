#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""For-looping a Simple data"""


import decimal


def lexicographics(to_analyze):
    """This is a for loop for a simple data.

    This function provides the maxium, minumum, and average length of words
    in a speech performing a lexicograshical analysis.

    Args:
        to_analyze(mixed): provides texts.

    Returns:
        The maximum and minimum number of words, and average number of words
        per line in to_analyze.

    Examples:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4.0))

        >>> import task_03
        >>> import data
        >>> task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))

    """
    split_comma = to_analyze.split('\n')
    sum_line = 0
    length_list = []
    for item in split_comma:
        line_length = len(item.split(' '))
        sum_line += line_length
        length_list.append(line_length)
    max_num = max(length_list)
    min_num = min(length_list)
    avg_num = decimal.Decimal(sum_line) / len(split_comma)
    return max_num, min_num, avg_num
