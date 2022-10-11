#!/usr/bin/python
# -*- coding: utf-8 -*-

# File name: bpmSnake.py
# Author: BigTajine
# Date created: 01/10/2022
# Date last modified: 11/10/2022
# Python version: 3.10.7

"""
bpmSnake; what will the snake give?
GUI coming soon!
"""

from random import randrange

print('---------------')
bpm_input_low = int(input("Give me a bpm between "))
bpm_input_high = int(input("and "))
print('---------------')
print("bpm: "+str(randrange(bpm_input_low, bpm_input_high)))
print('---------------')