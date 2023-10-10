from gurobipy import * 
import gurobipy as gp
import numpy as np
import random

def affectation_utilité (matrice) : 
    d = dict()
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            d[i,j] = matrice[i][j]
    return d

def max_l(matrice): 
    regret = []
    for i in range(len(matrice)): 
        regret.append(max(matrice[i]))
    return regret
    
def alloue_matrice (n):
    matrice = np.zeros((n,n),int)
    for i in range(n): 
        for j in range(n): 
            matrice [i,j] = random.randint(1, 21)
    return matrice 

  






