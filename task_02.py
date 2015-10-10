#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""If and Else Statement"""


def bool_to_str(bval):
    """If and Else Statement
    This function returns a 'Yes' or 'No' value, equivalent of truthy and
    falsy values.

    Args:
        bval(mixed): value to be tested in if and else statement.

    Returns:
        str: a string Yes or No

    Examples:
        >>>import task_02
        >>>task_02.bool_to_str(True)
        'Yes'

        >>>import task_02
        >>>task_02.bool_to_str(' ')
        'No'

        >>>import task_02
        >>>task_02.bool_to_str(False)
        'No'

    """
    aye_or_nay = 'Yes'
    if bval is True:
        aye_or_nay = 'Yes'
    else:
        aye_or_nay = 'No'
    return aye_or_nay
