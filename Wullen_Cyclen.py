# Cycle graph subset length portion of ROBDD computation
import numpy as np
"""Importing numpy for np.random probability functions"""
from pyeda.boolalg.bdd import _expr2bddnode
"""importing _expr2bddnode from TT-expr-node conversion"""
from pyeda.inter import *
"""Importing pyeda for BDDs/TT/variable assignment"""


def Wullen_Cyclen(n):
    """Takes input n, Constructs a ROBDD associated in which
    paths to 1 from the root represent an independent subset of nodes of Cn;
    where Cn is a cycle graph with vertex set of length n"""
    print("Running Cyclen")
    a, b, c, d, w, x, y, z = map(exprvar, 'abcdwxyz')
    if n == 6:
        itered = list(iter_points([a, b, c, x, y, z]))
    elif n == 8:
        itered = list(iter_points([a, b, c, d, w, x, y, z]))
    print(itered)
    # for reference the finite set below contains the available ind sets for n=6
    finiteSet6 = ["101010", "010101", "100100", "101000", "100010", "010010",
                  "010100", "010001", "001010", "001001", "000101"]

    finiteSet8 = ["101010", "010101", "100100", "101000", "100010", "010010",
                  "010100", "010001", "001010", "001001", "000101"] # needs to be updated
    finSetIn = []
    if n == 6:
        #finSetIn = "".join(finiteSet6)
        #finSetIn = finSetIn + "1"
        finSetIn = finiteSet6
    elif n == 8:
        finSetIn = "1".join(finiteSet8)
        finSetIn = finSetIn + "1"
    TTlistAdapted = []
    for i in itered:
        for j in finSetIn:
            if i == j:  # comparison not quite returning correctly yet
                TTlistAdapted.append('1')
            else:
                TTlistAdapted.append('0')
    print(TTlistAdapted)
    a = ttvar('a')
    b = ttvar('b')
    c = ttvar('c')
    d = ttvar('d')
    w = ttvar('w')
    x = ttvar('x')
    y = ttvar('y')
    z = ttvar('z')
    TT = []
    if n == 6:
        TT = truthtable([a, b, c, x, y, z], TTlistAdapted)
    elif n == 8:
        TT = truthtable([a, b, c, d, w, x, y, z], TTlistAdapted)
    f = truthtable2expr(TT)
    F = expr2bdd(f)
    print(TT)

