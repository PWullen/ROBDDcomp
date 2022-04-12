# SAT Count f(x)=1 computation
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
    print("The random Bernoulli output for p = ", p)
    print(arr)
    print("The Truth Table generated from the Bernoulli trials")
    print(TT)
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


def TT_BDD_init_short(n, p):
    """
    TT_init_short generates a set of n variables to a truth table matrix based
    on the probability p of any variable equaling 1 -- with a specific adaption to
    not pull over any print statements for the purpose of Achilles Heel testing
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
    f = truthtable2expr(TT)  # pulling TT values and making expression
    F = expr2bdd(f)  # pulling expression values to make BDD
    return F

def AH6(p):
    """
    Achilles Heel function utilizing 6 variables a,b,c,x,y,z
    for first ordering a<b<c...

    And(Or(a, b), Or(c, x), Or(y, z))
    """
    BDD = TT_BDD_init_short(64, p)

    a = exprvar('a')
    b = exprvar('b')
    c = exprvar('c')
    x = exprvar('x')
    y = exprvar('y')
    z = exprvar('z')
    f = And(Or(a, b), Or(c, x), Or(y, z))
    print(f)
    ah = AchillesHeel(a,b,c,x,y,z)
    print(ah)
    return f


def Wullen_Count(p):
    """Takes BDD as list:
    Returns count of number of solutions to f(x)=1 and
    returns vector of length n that shows the number 1's in each bead of BDD"""
    BDD = TT_BDD_init(64, p)  # n=64 for 6 variable TT construction
    print("The BDD generated from 6 variables with probability of 1 = ", p)
    print(BDD.to_dot())
    print("The Achilles Heel construction of these 6 variables is =")
    AH6(p)
    """The following is all not according to the prompt, but can be used as a self check"""
    #print("The list of all satisfying f(x)=1")
    #print(list(BDD.satisfy_all()))
    #count = 0
    #for i in BDD.satisfy_all():
    #    print(i)
    #    count += 1
    #print("The total number of satisfying f(x)=1 is ", count)
    """Can now continue to print out the ROBDD with each node annotated with 
    the number solutions associated with that node"""







