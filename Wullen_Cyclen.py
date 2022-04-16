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

    a, b, c, d, w, x, y, z = map(exprvar, 'abcdwxyz')
    itered = []
    if n == 6:
        itered = list(iter_points([a, b, c, x, y, z]))
    elif n == 8:
        itered = list(iter_points([a, b, c, d, w, x, y, z]))
    #print(itered)
    # setup for hardcoded pre-solved ind set
    finiteSet6 = ["101010", "010101", "100100", "101000", "100010", "010010",
                  "010100", "010001", "001010", "001001", "000101"]
    finiteSet6shadow = [{a: 1, b: 0, c: 0, x: 0, y: 0, z: 0}, {a: 0, b: 1, c: 0, x: 0, y: 0, z: 0}, {a: 0, b: 0, c: 1, x: 0, y: 0, z: 0},
                        {a: 0, b: 0, c: 0, x: 1, y: 0, z: 0}, {a: 0, b: 0, c: 0, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 0, x: 0, y: 0, z: 1},
                        {a: 1, b: 0, c: 1, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, x: 1, y: 0, z: 1}, {a: 1, b: 0, c: 1, x: 0, y: 0, z: 0},
                        {a: 1, b: 0, c: 0, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, x: 1, y: 0, z: 0},
                        {a: 0, b: 1, c: 0, x: 0, y: 0, z: 1}, {a: 0, b: 0, c: 1, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 1, x: 0, y: 0, z: 1},
                        {a: 0, b: 0, c: 0, x: 1, y: 0, z: 1}, {a: 1, b: 0, c: 0, x: 1, y: 0, z: 0}]
    finiteSet8 = ["101010", "010101", "100100", "101000", "100010", "010010",
                  "010100", "010001", "001010", "001001", "000101"] # needs to be updated
    finiteSet8shadow = []
    finSetIn = []
    if n == 6:
        finSetIn = finiteSet6shadow
    elif n == 8:
        finSetIn = finiteSet8shadow

    TTlistAdapted = []
    for _ in itered:
        TTlistAdapted.append(0)  # init TT list to all 0 outputs
    for i in range(len(TTlistAdapted)):  # index of TT list created
        for j in range(len(finSetIn)):  # index of iterated set
            finKeys = finSetIn[j].items()
            #print(finKeys)
            for k in range(len(itered)):  # index of finite ind set
                iterKeys = itered[k].items()
                if finKeys == iterKeys:
                    TTlistAdapted[k] = 1
    #print(TTlistAdapted)
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
    # conversion from TT to BDD
    f = truthtable2expr(TT)
    F = expr2bdd(f)
    #print(TT)  #can uncomment for TT printout
    print(F.to_dot())

