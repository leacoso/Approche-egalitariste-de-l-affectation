from gurobipy import * 
import gurobipy as gp
import numpy as np
from PL import *
matrice = np.array([[12,20,6,5,8],[5,12,6,8,5],[8,5,11,5,6],[6,8,6,11,5],[5,6,8,7,7]])

def moyenne(d,n): 

    # Création du Modele
    m = gp.Model()

    #Création des variables
    x = {}
    for i in range (n):
        for j in range( n):
            x[i,j]= m.addVar(vtype = 'B', name = "x"+str(i+1)+str(j+1))

    m.update()


    # Fonction objective

    m.setObjective((gp.quicksum((gp.quicksum(x[i,j]*d[i,j] for j in range(n))) for i in range(n)))/n, gp.GRB.MAXIMIZE)

    # Contraintes
    for i in range(n):
        m.addConstr(gp.quicksum(x[i,j] for j in range(n)) == 1, name="c0")
    for j in range( n):
        m.addConstr(gp.quicksum(x[i,j] for i in range(n)) == 1, name="c1")


    # Resolution
    m.optimize()
    m.printAttr('X')
    output = []
    print(output)
    print("Obj:  ",m.objVal)

#d = alloue_matrice(10)
#moyenne(d,10)
