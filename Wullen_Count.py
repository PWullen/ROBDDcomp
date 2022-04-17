#!/usr/bin/env python3
# SAT Count f(x)=1 computation
import numpy as np
from pyeda.inter import *
import IPython
import graphviz
import gvmagic
import pydot
import pandas as pd
"""Importing numpy for np.random probability functions
   Importing pyeda.inter for logical operations
   Importing Ipython, graphviz, and gvmagic (+dependencies) for BDD visualization"""


def prob_init(n, p):
    """
    prob_init will take n as the number of variables and p as the probability, to create a set of bernoulli trials
    to append to a list.
    """
    arr = []  # init probability list
    for i in range(n):
        i = np.random.binomial(1, p)  # utilizing Binomial of n=1 allows
        # for each i to be a Bernoulli trial
        arr.append(i)
    return arr


def TT_BDD_init(n, p):
    """
    TT_BDD_init generates a truth table matrix based
    on the probability p of any variable equaling 1 and
    a set of n bits, where n=2^k for k variables.
    """
    arr = prob_init(n, p)
    # init TT vars
    a, b, c, x, y, z = map(ttvar, 'abcxyz')
    TT = truthtable([a, b, c, x, y, z], arr)

    """The following lines can be uncommented for verification
    of the Bernoulli trials to formulate the 64bit TT"""
    #print("The random Bernoulli output for p = ", p)
    #print(arr)
    #print("The Truth Table generated from the Bernoulli trials")
    #print(TT)

    f = truthtable2expr(TT)  # pulling TT values and making expression
    F = expr2bdd(f)  # pulling expression values to make BDD

    """The following lines can be uncommented to view the expression generated
    from the TT values, and the following BDD generated from the expression"""
    #print(f)  # expression generated from TT
    #print(F.to_dot())  # .to_dot() GraphViz BDD visualization
    return F


def AH6(BDD):
    """
    Achilles Heel function utilizing 6 variables a,b,c,x,y,z
    for first ordering a<b<c...

    And(Or(a, b), Or(c, x), Or(y, z))
    """
    F = bdd2expr(BDD)
    #print("Expression from BDD:")
    #print(F)
    # init expression variables
    a, b, c, x, y, z = map(exprvar, 'abcxyz')
    f = And(Or(a, b), Or(c, x), Or(y, z))  # logical expression of Achilles Heel
    print("Achilles Heel of expression:")
    print(f)
    ah = AchillesHeel(a, b, c, x, y, z, simplify=True)  # PyEDA built in Achilles Heel
    """Can uncomment line below for equivalence confirmation of Achilles Heel function
    made versus built in PyEDA Achilles Heel"""
    #print(ah)  # built-in PyEDA Achilles Heel
    return f


def Wullen_Count(p):
    """Takes input p= probability of Bernoulli trial=1
    then initializes BDD based on init function TT_BDD_init
    Returns count of number of solutions to f(x)=1 and
    returns vector of length n that shows the number 1's in each bead of BDD"""

    BDD = TT_BDD_init(64, p)  # n=64 for 6 variable TT construction
    AH6(BDD)  # Achilles Heel for 6 variables
    """Can uncomment line below to verify count working correctly"""
    #print(list(BDD.satisfy_all()))
    count = 0
    for _ in BDD.satisfy_all():
        count += 1
    print("The total number of satisfying f(x)=1 is ", count)
    """ROBDD vector for node contributions to solutions incomplete
    latest iteration below commented out"""
    #countval = 0
    #dd = []
    #for paths in BDD.satisfy_all():
        #counts = dict()
        #pathCache = [paths.values()]  # list for paths.items()
        #for d in pathCache:  # each path in cache iterates as dict
            #dd.append(d)
    #print(dd)
