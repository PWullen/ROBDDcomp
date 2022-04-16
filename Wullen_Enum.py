# Enumeration portion of ROBDD computation

from pyeda.boolalg.bdd import _expr2bddnode

from Wullen_Count import prob_init
"""Importing TT/BDD initialization """
"""importing _expr2bddnode from TT-expr-node conversion"""
from pyeda.inter import *
"""Importing pyeda for BDDs/TT/variable assignment"""


"""
def findpath(start, end, path=tuple()):
    
    #path will
    
    path = path + (start, )
    if start is end:
        return path
    else:
        ans = None
        if start.lo is not None:
            ans = findpath(start.lo, end, path)
        if ans is None and start.hi is not None:
            ans = findpath(start.hi, end, path)
        return ans

def enum_paths(start, end, path=tuple()):
    #Iterate through all paths from start to end.
    path = path + (start, )
    if start is end:
        yield path
    else:
        nodes = [start.lo, start.hi]
        for node in nodes:
            if node is not None:
                yield from enum_paths(node, end, path)
"""

"""
def TT_BDD_init(n, p):
    """"""
    #TT_init generates a set of n variables to a truth table matrix based
    #on the probability p of any variable equaling 1.
    """"""
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
    ff = _expr2bddnode(f)
    #pathfound = findpath(1,-1,f)
    #print("Now printing path found",pathfound)
    return F
    #%dotobj ff = F #from PyEDA documentation -- currently not operational
    #print(F)
    #return TT
    #AH = AchillesHeel(a, b, c, x, y, z)
    #print(AH.to_cnf())
"""

def Wullen_Enum(p):
    """Takes BDD as list:
    Enumerates in lexicographic order, all vectors (x1,x2,...,xn)
    for which f(x1,x2,...,xn)=1"""
    print("Running Enum for probability", p)
    arr = prob_init(64, p)
    #BDD = TT_BDD_init(64, p)  # n: (2^6=64)
    a, b, c, x, y, z = map(ttvar, 'abcxyz')
    TT = truthtable([a, b, c, x, y, z], arr)
    f = truthtable2expr(TT)  # pulling TT values and making expression
    F = expr2bdd(f)  # pulling expression values to make BDD
    print("The list of all satisfying f(x)=1 paths")
    for i in F.satisfy_all():
        print(i)
