#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""For-looping a Simple data"""


import data
import decimal
to_analyze = ('''Don't stop believing, Hold on to that feeling.''')

def lexicographics(to_analyze):
    to_analyze_split_comma = to_analyze.split(', ')
    split_space = to_analyze.split (' ') 
    myind = 0
    for item in to_analyze_split_comma:
        myind += 1
        print myind, item
