# ROBDD computation
# Peter Wullen

import os
import numpy as np
from pyeda.inter import *
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



def AH8():
    """
    Achilles Heel function utilizing 8 variables a,b,c,d,w,x,y,z
    for first ordering a<b<c...

    And(Or(a, b), Or(c, d), Or(w, x), Or(y, z))
    """
    a = exprvar('a')
    b = exprvar('b')
    c = exprvar('c')
    d = exprvar('d')
    w = exprvar('w')
    x = exprvar('x')
    y = exprvar('y')
    z = exprvar('z')
    f = And(Or(a, b), Or(c, d), Or(w, x), Or(y, z))
    return f




def testdebug():
    print('Testing Wullen_Count.py\n')
    print('Running test with p=0.1 for f(x)=1\n')
    Wullen_Count(0.1)
    Wullen_Enum(0.1)
    Wullen_Cyclen(6)
"""    print('Running test with p=0.3 for f(x)=1')
    Wullen_Count(0.3)
    print('Running test with p=0.5 for f(x)=1')
    Wullen_Count(0.5)
    print('Running test with p=0.8 for f(x)=1')
    Wullen_Count(0.8)
    print('Testing Wullen_Enum.py')
    print('Running test with p=0.1 for f(x)=1')
    Wullen_Enum(0.1)
    print('Running test with p=0.3 for f(x)=1')
    Wullen_Enum(0.3)
    print('Running test with p=0.5 for f(x)=1')
    Wullen_Enum(0.5)
    print('Running test with p=0.8 for f(x)=1')
    Wullen_Enum(0.8)
    print('Testing Wullen_Cyclen.py')
    print('Testing for C_6; n=6')
    Wullen_Cyclen()
    print('Testing for C_8; n=8')
    Wullen_Cyclen()
"""
if __name__ == '__main__':
    testdebug()
