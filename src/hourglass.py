#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maximum = -999

    for row in range(0,4):
        for column in range(0,4):
            hourglass = sum(arr[row][column:column + 3]) \
                      + arr[row + 1][column + 1] \
                      + sum(arr[row+ 2][column:column + 3])
            maximum = hourglass if hourglass > maximum else maximum

    return maximum

if __name__ == '__main__':

    arr = [ \
        [-1, -1, 0, -9, -2, -2], \
        [-1, -1, 0, -9, -2, -2], \
        [-1, -1, -1, -2, -3, -4], \
        [-1, -9, -2, -4, -4, -5], \
        [-7, -3, -3, -2, -9, -9], \
        [-1, -3, -1, -2, -4, -5] \
    ]

    result = hourglassSum(arr)
    print(result)
