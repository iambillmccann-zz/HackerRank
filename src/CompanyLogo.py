#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    the_letters = {}
    total = len(s)

    for character in s:
        if character in the_letters: continue
        else: the_letters[character] = s.count(character)

    frequencies = sorted(the_letters.items(), key = lambda kv:(total - kv[1], kv[0]))
    count = 0
    for item in frequencies:
        count += 1
        print(item[0], item[1])
        if count >= 3: break