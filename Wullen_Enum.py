# Enumeration portion of ROBDD computation
import numpy as np
"""Importing numpy for np.random probability functions"""
from pyeda.inter import *
"""Importing pyeda for BDDs/TT/variable assignment"""


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


def Wullen_Enum(p):
    """Takes BDD as list:
    Enumerates in lexicographic order, all vectors (x1,x2,...,xn)
    for which f(x1,x2,...,xn)=1"""
    print("Running Enum")
    BDD = TT_BDD_init(64, p)  # n: (2^6=64; 2^8=256)

