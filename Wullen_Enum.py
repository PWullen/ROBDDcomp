#!/usr/bin/env python3
# Enumeration portion of ROBDD computation

from Wullen_Count import prob_init
"""Importing TT/BDD initialization """
from pyeda.inter import *
"""Importing pyeda for BDDs/TT/variable assignment"""
import IPython
import graphviz
import gvmagic
import pydot
import pandas as pd
"""Importing Ipython, graphviz, and gvmagic (+dependencies) for BDD visualization"""

def Wullen_Enum(p):
    """Takes BDD as list:
    Enumerates in lexicographic order, all vectors (x1,x2,...,xn)
    for which f(x1,x2,...,xn)=1"""
    print("Running Enum for probability", p)
    arr = prob_init(64, p)
    """For probability list uncomment below """
    #print(arr)
    a, b, c, x, y, z = map(ttvar, 'abcxyz')
    TT = truthtable([a, b, c, x, y, z], arr)
    """For truth table uncomment below """
    #print(TT)
    f = truthtable2expr(TT)  # pulling TT values and making expression
    """For logic expression uncomment below """
    #print(f)
    F = expr2bdd(f)  # pulling expression values to make BDD
    """For bdd uncomment below """
    #print(F.to_dot)  # .to_dot() GraphViz BDD visualization
    print("The list of all satisfying f(x)=1 paths")
    for i in F.satisfy_all():
        print(i)
