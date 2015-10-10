#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Fibonacci Sequence"""


def fibonacci(maxint):
    """A Fibonacci Sequence
    This is a Fionbacci number sequence generating function with a while loop.

    Args:
        maxint(int): sets the maximum interger for function to stop when
        condition is not longer met.

    Returns:
        int: a list of interger being appended by the result of while loop.

    Examples:
        >>>import task_01
        >>>task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>>task_01.fibonacci(22)
        [0, 1, 1, 2, 3, 5, 8, 13, 21]

    """
    mylist = [0, ]
    mya, myb = 0, 1
    while myb < maxint:
        mylist.append(myb)
        mya, myb = myb, mya + myb
    return mylist
