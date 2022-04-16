# Cycle graph subset ROBDD computation
from pyeda.inter import *
import IPython
import graphviz
import gvmagic
import pydot
import pandas as pd
"""Importing pyeda for BDDs/TT/variable assignment
Importing Ipython, graphviz, and gvmagic (+dependencies) for BDD visualization"""

def Wullen_Cyclen(n):
    """Takes input n, Constructs a ROBDD associated in which
    paths to 1 from the root represent an independent subset of nodes of Cn;
    where Cn is a cycle graph with vertex set of length n.

    Presently only works for inputs 6 and 8, as interior set calculation is hard-coded"""

    a, b, c, d, w, x, y, z = map(exprvar, 'abcdwxyz')
    itered = []
    if n == 6:
        itered = list(iter_points([a, b, c, x, y, z]))
    elif n == 8:
        itered = list(iter_points([a, b, c, d, w, x, y, z]))
    #print(itered)
    # setup for hardcoded solved ind set via handwritten work
    # this is extremely pedantic and not ideal for code
    finiteSet6shadow = [{a: 1, b: 0, c: 0, x: 0, y: 0, z: 0}, {a: 0, b: 1, c: 0, x: 0, y: 0, z: 0}, {a: 0, b: 0, c: 1, x: 0, y: 0, z: 0}, {a: 0, b: 0, c: 0, x: 1, y: 0, z: 0}, {a: 0, b: 0, c: 0, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 0, x: 0, y: 0, z: 1}, {a: 1, b: 0, c: 1, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, x: 1, y: 0, z: 1}, {a: 1, b: 0, c: 1, x: 0, y: 0, z: 0},
                        {a: 1, b: 0, c: 0, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, x: 1, y: 0, z: 0}, {a: 0, b: 1, c: 0, x: 0, y: 0, z: 1}, {a: 0, b: 0, c: 1, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 1, x: 0, y: 0, z: 1}, {a: 0, b: 0, c: 0, x: 1, y: 0, z: 1}, {a: 1, b: 0, c: 0, x: 1, y: 0, z: 0}]

    finiteSet8shadow = [{a: 1, b: 0, c: 0, d: 0, w: 0, x: 0, y: 0, z: 0}, {a: 0, b: 1, c: 0, d: 0, w: 0, x: 0, y: 0, z: 0}, {a: 0, b: 0, c: 1, d: 0, w: 0, x: 0, y: 0, z: 0}, {a: 0, b: 0, c: 0, d: 1, w: 0, x: 0, y: 0, z: 0}, {a: 0, b: 0, c: 0, d: 0, w: 1, x: 0, y: 0, z: 0}, {a: 0, b: 0, c: 0, d: 0, w: 0, x: 1, y: 0, z: 0}, {a: 0, b: 0, c: 0, d: 0, w: 0, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 0, d: 0, w: 0, x: 0, y: 0, z: 1},
                        {a: 1, b: 0, c: 1, d: 0, w: 1, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, d: 1, w: 0, x: 1, y: 0, z: 1},
                        {a: 1, b: 0, c: 1, d: 0, w: 1, x: 0, y: 0, z: 0}, {a: 1, b: 0, c: 1, d: 0, w: 0, x: 1, y: 0, z: 0}, {a: 1, b: 0, c: 1, d: 0, w: 0, x: 0, y: 1, z: 0}, {a: 1, b: 0, c: 0, d: 1, w: 0, x: 1, y: 0, z: 0}, {a: 1, b: 0, c: 0, d: 1, w: 0, x: 0, y: 1, z: 0}, {a: 1, b: 0, c: 0, d: 0, w: 1, x: 0, y: 1, z: 0}, {a: 1, b: 0, c: 0, d: 0, w: 1, x: 0, y: 1, z: 0},
                        {a: 0, b: 1, c: 0, d: 1, w: 0, x: 1, y: 0, z: 0}, {a: 0, b: 1, c: 0, d: 1, w: 0, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, d: 1, w: 0, x: 0, y: 0, z: 1}, {a: 0, b: 1, c: 0, d: 0, w: 1, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, d: 0, w: 1, x: 0, y: 0, z: 1}, {a: 0, b: 1, c: 0, d: 0, w: 0, x: 1, y: 0, z: 1},
                        {a: 0, b: 0, c: 1, d: 0, w: 1, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 1, d: 0, w: 1, x: 0, y: 0, z: 1}, {a: 0, b: 0, c: 1, d: 0, w: 0, x: 1, y: 0, z: 1}, {a: 0, b: 0, c: 0, d: 1, w: 0, x: 1, y: 0, z: 1},
                        {a: 1, b: 0, c: 1, d: 0, w: 0, x: 0, y: 0, z: 0}, {a: 1, b: 0, c: 0, d: 1, w: 0, x: 0, y: 0, z: 0}, {a: 1, b: 0, c: 0, d: 0, w: 1, x: 0, y: 0, z: 0}, {a: 1, b: 0, c: 0, d: 0, w: 0, x: 1, y: 0, z: 0}, {a: 1, b: 0, c: 0, d: 0, w: 0, x: 0, y: 1, z: 0}, {a: 1, b: 0, c: 0, d: 0, w: 0, x: 0, y: 0, z: 1},
                        {a: 0, b: 1, c: 0, d: 1, w: 0, x: 0, y: 0, z: 0}, {a: 0, b: 1, c: 0, d: 0, w: 1, x: 0, y: 0, z: 0}, {a: 0, b: 1, c: 0, d: 0, w: 0, x: 1, y: 0, z: 0}, {a: 0, b: 1, c: 0, d: 0, w: 0, x: 0, y: 1, z: 0}, {a: 0, b: 1, c: 0, d: 0, w: 0, x: 0, y: 0, z: 1},
                        {a: 0, b: 0, c: 1, d: 0, w: 1, x: 0, y: 0, z: 0}, {a: 0, b: 0, c: 1, d: 0, w: 0, x: 1, y: 0, z: 0}, {a: 0, b: 0, c: 1, d: 0, w: 0, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 1, d: 0, w: 0, x: 0, y: 0, z: 1},
                        {a: 0, b: 0, c: 0, d: 1, w: 0, x: 1, y: 0, z: 0}, {a: 0, b: 0, c: 0, d: 1, w: 0, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 0, d: 1, w: 0, x: 0, y: 0, z: 1},
                        {a: 0, b: 0, c: 0, d: 0, w: 1, x: 0, y: 1, z: 0}, {a: 0, b: 0, c: 0, d: 0, w: 1, x: 0, y: 0, z: 1}, {a: 0, b: 0, c: 0, d: 0, w: 0, x: 1, y: 0, z: 1},
                        ]
    finSetIn = []
    if n == 6:
        finSetIn = finiteSet6shadow
    elif n == 8:
        finSetIn = finiteSet8shadow

    TTlistAdapted = []
    for _ in itered:
        TTlistAdapted.append(0)  # init TT list to all 0 outputs

    for i in range(len(TTlistAdapted)):  # index of TT list created
        for j in range(len(finSetIn)):  # index of finite ind set
            finKeys = finSetIn[j].items()
            for k in range(len(itered)):  # index of iterated set
                iterKeys = itered[k].items()
                if finKeys == iterKeys:
                    TTlistAdapted[k] = 1
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
