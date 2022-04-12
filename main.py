# ROBDD computation of f(x) = 1
#Peter Wullen

import os
"""Importing OS for file-checking"""
import numpy as np
"""Importing numpy for np.random probability functions"""
from pyeda.inter import *
"""Importing pyeda for BDDs/TT/variable assignment"""
from Wullen_Count import Wullen_Count
"""Importing count function"""
from Wullen_Enum import Wullen_Enum
"""Importing enumeration function"""
from Wullen_Cyclen import Wullen_Cyclen
"""Importing cyclen function"""
import IPython
import graphviz
import gvmagic
import pydot
import pandas as pd

"""Importing Ipython, graphviz, and gvmagic (+dependencies) for BDD visualization"""


def TT_BDD_init(n, p):
    """
    TT_init generates a set of n variables to a truth table matrix based
    on the probability p of any variable equaling 1.
    """
    arr = []
    for i in range(n):
        i = np.random.binomial(1, p)  # utilizing Binomial of n=1 allows
        # for each i to be a Bernoulli trial
        arr.append(i)
    a = ttvar('a')
    b = ttvar('b')
    c = ttvar('c')
    x = ttvar('x')
    y = ttvar('y')
    z = ttvar('z')
    TT = truthtable([a, b, c, x, y, z], arr)
    #print(arr)
    #print(TT)
    f = truthtable2expr(TT)  # pulling TT values and making expression
    #print(f)
    F = expr2bdd(f)  # pulling expression values to make BDD
    #print(F.to_dot())
    return F
    #%dotobj ff = F #from PyEDA documentation -- currently not operational
    #print(F)
    #return TT
    #AH = AchillesHeel(a, b, c, x, y, z)
    #print(AH.to_cnf())


def AH6():
    """
    Achilles Heel function utilizing 6 variables a,b,c,x,y,z
    for first ordering a<b<c...

    And(Or(a, b), Or(c, x), Or(y, z))
    """
    a = exprvar('a')
    b = exprvar('b')
    c = exprvar('c')
    x = exprvar('x')
    y = exprvar('y')
    z = exprvar('z')
    f = And(Or(a, b), Or(c, x), Or(y, z))
    return f


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
