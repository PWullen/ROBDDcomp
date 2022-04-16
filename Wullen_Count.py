# SAT Count f(x)=1 computation

import numpy as np
from pyeda.boolalg.bdd import _expr2bddnode
from pyeda.inter import *
"""Importing numpy for np.random probability functions
   Importing expr2bddnode for DFS operations
   Importing pyeda.inter for logical operations"""


def TT_BDD_init(n, p):
    """
    TT_BDD_init generates a truth table matrix based
    on the probability p of any variable equaling 1 and
    a set of n bits, where n=2^k for k variables.
    """
    arr = []  # init probability list
    for i in range(n):
        i = np.random.binomial(1, p)  # utilizing Binomial of n=1 allows
        # for each i to be a Bernoulli trial
        arr.append(i)
    # init TT vars
    a = ttvar('a')
    b = ttvar('b')
    c = ttvar('c')
    x = ttvar('x')
    y = ttvar('y')
    z = ttvar('z')
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
    #print(F.to_dot())  # BDD generated from expression to be output by GraphViz

    """Below is the attempt at going the long way around from satisfy_all"""
    ff = _expr2bddnode(f)
    #print("")
    #print("Now printing made dfs\n")
    a = bddvar('a')
    b = bddvar('b')
    c = bddvar('c')
    x = bddvar('x')
    y = bddvar('y')
    z = bddvar('z')
    #BDDdfs(ff)

    return F


def AH6(BDD):
    """
    Achilles Heel function utilizing 6 variables a,b,c,x,y,z
    for first ordering a<b<c...

    And(Or(a, b), Or(c, x), Or(y, z))
    """
    F = bdd2expr(BDD)
    print("Expression from BDD:")
    print(F)
    # init expression variables
    a = exprvar('a')
    b = exprvar('b')
    c = exprvar('c')
    x = exprvar('x')
    y = exprvar('y')
    z = exprvar('z')
    Fexpand = []
    variables = a, b, c, x, y, z
    #for variables in F:
        #Fexpand.append(variables)
    f = And(Or(a, b), Or(c, x), Or(y, z))  # logical expression of Achilles Heel

    print("Achilles Heel of expression:")
    #aH = AchillesHeel(Fexpand)
    #print(aH)
    print(f)
    ah = AchillesHeel(a, b, c, x, y, z, simplify=True)  # PyEDA built in Achilles Heel
    """Can uncomment line below for equivalence confirmation of Achilles Heel function
    made versus built in PyEDA Achilles Heel"""
    #print(ah)
    return f

def BDDdfs(BDDNode):
    """
    BDDdfs will perform a preorder depth-first-search to identify the tuple of
    (vk,lk,hk) outlined to be vk = node id, lk = instructions for vk=0, hk = instructions for vk=1
    (which also correspond to the nodes pointed to by the root vk) and print these values.
    BDDdfs takes the PyEDA class BDDNode as input and utilizes the class behavior to assign
    root, lo, and hi.
    """
    if BDDNode is None:
        return
    else:
        print(BDDNode.root)
        BDDdfs(BDDNode.lo)
        BDDdfs(BDDNode.hi)


def Wullen_Count(p):
    """Takes input p= probability of Bernoulli trial=1
    then initializes BDD based on init function TT_BDD_init
    Returns count of number of solutions to f(x)=1 and
    returns vector of length n that shows the number 1's in each bead of BDD"""
    BDD = TT_BDD_init(64, p)  # n=64 for 6 variable TT construction (code in main)
    AH6(BDD)  # Achilles Heel for 6 variables (code in main)
    """Can uncomment line below to verify count working correctly"""
    #print(list(BDD.satisfy_all()))
    count = 0
    for i in BDD.satisfy_all():
        count += 1
    print("The total number of satisfying f(x)=1 is ", count)
    """Can now continue to print out the ROBDD with each node annotated with 
    the number solutions associated with that node"""


