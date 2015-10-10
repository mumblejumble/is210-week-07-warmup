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

        >>> import task_03
        >>> task_03.lexicographics('''Don't stop, believing,
        Hold on to that feeling,
        don't remember the other lyrics.
        OOooooohhhh.''')
        (5, 1, Decimal('3.5'))

    """
    split_comma = to_analyze.split('\n')
    length_list = []
    for item in split_comma:
        line_length = len(item.split(' '))
        length_list.append(line_length)
    return (max(length_list), min(length_list),
            sum(length_list)/decimal.Decimal(len(length_list)))
