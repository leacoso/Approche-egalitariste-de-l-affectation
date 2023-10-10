from gurobipy import * 
import gurobipy as gp
import numpy as np
from PL import *
#epsilon =  0.005
epsilon =2.220446049250313e-16

def f(d,n): 
# Création du Modele
    m = gp.Model()

#Création des variables
    x = {}
    l = {}


    for i in range (n):
        l[i]= m.addVar(vtype = gp.GRB.CONTINUOUS, name = "l"+str(i+1))
        for j in range(n):
            x[i,j]= m.addVar(vtype = gp.GRB.BINARY, name = "x"+str(i+1)+str(j+1))
        
        
    mini = m.addVar(vtype = gp.GRB.CONTINUOUS, name = "mini")

    m.update()

    # Fonction objective
    m.setObjective( mini +  epsilon*gp.quicksum((gp.quicksum(x[i,j]*d[i,j] for j in range(n))) for i in range(n)), gp.GRB.MAXIMIZE)

    # Contraintes
    for i in range(n):
        m.addConstr(gp.quicksum(x[i,j] for j in range(n) ) == 1)
    for j in range(n):
        m.addConstr(gp.quicksum(x[i,j] for i in range(n)) == 1)


    for i in range(n): 
        for j in range(n): 
            m.addConstr((x[i,j] == 1) >> (l[i] == d[i,j]))
        
    m.addConstr( mini == gp.min_( l[i] for i in range(n) ))

    # Resolution
    m.optimize() 
    m.printAttr('X')
    print("Obj: ",m.objVal)
    
#d = np.array([[1,3,1000], [0,20,0], [0,0,3]])
d2 = np.array([[1,2,3,4],[2,3,4,5],[3,4,10000,5],[4,5,6,7]])
f(d2,4)
