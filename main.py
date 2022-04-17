#!/usr/bin/env python3
# ROBDD computation
# Peter Wullen
from Wullen_Count import Wullen_Count
from Wullen_Enum import Wullen_Enum
from Wullen_Cyclen import Wullen_Cyclen
import IPython
import graphviz
import gvmagic
import pydot
import pandas as pd
"""Importing OS for file-checking
Importing numpy for np.random probability functions
Importing pyeda for BDDs/TT/variable assignment
Importing count function
Importing enumeration function
Importing cyclen function
Importing _expr2bddnode from node conversion
Importing Ipython, graphviz, and gvmagic (+dependencies) for BDD visualization"""


def testdebug():
    print('Testing Wullen_Count.py\n')
    print('\nRunning test with p=0.1 for f(x)=1\n')
    Wullen_Count(0.1)
    print('\nRunning test with p=0.3 for f(x)=1\n')
    Wullen_Count(0.3)
    print('\nRunning test with p=0.5 for f(x)=1\n')
    Wullen_Count(0.5)
    print('\nRunning test with p=0.8 for f(x)=1\n')
    Wullen_Count(0.8)
    print('\nTesting Wullen_Enum.py\n')
    print('Running test with p=0.1 for f(x)=1\n')
    Wullen_Enum(0.1)
    print('\nRunning test with p=0.3 for f(x)=1\n')
    Wullen_Enum(0.3)
    print('\nRunning test with p=0.5 for f(x)=1\n')
    Wullen_Enum(0.5)
    print('\nRunning test with p=0.8 for f(x)=1\n')
    Wullen_Enum(0.8)
    print('\nTesting Wullen_Cyclen.py\n')
    print('Testing for C_6; n=6\n')
    Wullen_Cyclen(6)
    print('\nTesting for C_8; n=8\n')
    Wullen_Cyclen(8)


if __name__ == '__main__':
    testdebug()
