# Cycle graph subset length portion of ROBDD computation
import numpy as np
"""Importing numpy for np.random probability functions"""
from pyeda.boolalg.bdd import _expr2bddnode
"""importing _expr2bddnode from TT-expr-node conversion"""
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
    print("The random Bernoulli output for p = ", p)
    print(arr)
    print("The Truth Table generated from the Bernoulli trials")
    print(TT)
    f = truthtable2expr(TT)  # pulling TT values and making expression
    #print(f)
    F = expr2bdd(f)  # pulling expression values to make BDD
    print(f)
    #print(F.to_dot())
    ff = _expr2bddnode(f)
    print("")
    print("Now printing made dfs\n")
    a = bddvar('a')
    b = bddvar('b')
    c = bddvar('c')
    x = bddvar('x')
    y = bddvar('y')
    z = bddvar('z')

    return F

def Wullen_Cyclen(n):
    """Takes input n, Constructs a ROBDD associated in which
    paths to 1 from the root represent an independent subset of nodes of Cn;
    where Cn is a cycle graph with vertex set of length n"""
    print("Running Cyclen")
    VertexSet = []
    for i in range(n):
        VertexSet.append(i)
    print(VertexSet)
    # for reference the finite set below contains the available ind sets for n=6
    finiteSet = ["101010", "010101", "100100", "101000", "100010", "010010",
                 "010100", "010001", "001010", "001001", "000101"]
    for j in finiteSet:
        finSetIn = "1".join(finiteSet)
    print(finSetIn)
    finiteSetTTin = "101010010101100100101000100010010010010100010001001010001001000101"
    print(finiteSetTTin)
    #this wont work with TT, input length is incorrect
    tvars = ttvars("x", n, n)
    TT = truthtable(tvars, finSetIn)
    f = truthtable2expr(TT)
    F = expr2bdd(f)
    print(F)

