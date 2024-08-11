import time
import argparse
import os
import sys
import logging
import json
from output import *
from arrayClass import *

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

    # args = parser.parse_args()
    # print(args.accumulate(args.integers))

    arr1 = Array([[1, 2], [3, 4]])
    arr2 = Array([[5, 6], [7, 8]])

    arr3 = arr1 * arr2
    arr3.display()

