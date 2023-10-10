from gurobipy import * 
import gurobipy as gp
import numpy as np
from PL import *
#epsilon =  2.220446049250313e-16
epsilon = 0.005

def g(d,n): 
    max_ligne = max_l(d)
    # Création du Modele
    m = gp.Model()

    #Création des variables
    x = {}
    regret = {}

    for i in range (n):
        regret[i] = m.addVar(vtype = gp.GRB.CONTINUOUS, name = "r"+str(i+1))
        for j in range(n):
            x[i,j]= m.addVar(vtype = gp.GRB.BINARY, name = "x"+str(i+1)+str(j+1))
    maxi = m.addVar(vtype = gp.GRB.CONTINUOUS, name = "maxi")
    m.update()

    # Fonction objective
    m.setObjective( maxi , gp.GRB.MINIMIZE)

    # Contraintes

    for i in range(n): 
        for j in range(n): 
            m.addConstr((x[i,j] == 1) >> (regret[i] == max_ligne[i] - d[i,j]))
        
    for i in range(n):
        m.addConstr(gp.quicksum(x[i,j] for j in range(n) ) == 1)
    
    for j in range(n):
        m.addConstr(gp.quicksum(x[i,j] for i in range(n)) == 1)

    m.addConstr(maxi == gp.max_(regret[i] for i in range(n) ))
    # Resolution
    m.optimize()
    m.printAttr('X')
    print("Obj: ",m.objVal)

#d2 = np.array([[1,2,3,4],[2,3,4,5],[3,4,10000,5],[4,5,6,7]])
#g(d2,4)

