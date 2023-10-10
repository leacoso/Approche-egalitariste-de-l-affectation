from gurobipy import * 
import gurobipy as gp
import numpy as np
from PL import *
import time 
import matplotlib.pyplot as plt
import numpy as np
import os
from moyenne1 import *
from f2 import *
from g3 import * 
epsilon =  2.220446049250313e-16

def courbe_moyenne(): 
    i = 2
    fich = open("temps_CPU_moyenne.txt", "w") 
    while i<400: 
        res = 0  
        for j in range(10): 
            matrice = alloue_matrice(i)
            start = time.time()
            moyenne(matrice,i)
            end = time.time()
            res = res +  (end-start)
        res = res /10
        fich.write(f"{i} {res} \n")
        i = i+5
    
    fich.close()


def trace_moyenne():
    (l1,l2) = lire("temps_CPU_moyenne.txt")
    plt.plot(l1, l2,label="COURBE MOYENNE")
    plt.legend()
    plt.title("Courbe du temps CPU en fonction de la taille de l'instance")
    plt.xlabel("Taille de l'instance")
    plt.ylabel("Temps CPU en secondes")
    plt.show() 
      

def courbe_f():
    i = 2
    fich = open("temps_CPU_f.txt", "w") 
    while i<100: 
        res = 0  
        for j in range(10): 
            matrice = alloue_matrice(i)
            start = time.time()
            f(matrice,i)
            end = time.time()
            res = res +  (end-start)
        res = res /10
        fich.write(f"{i} {res} \n")
        i = i+5
    
    fich.close()

    
def lire(txt) :
    l1 = []
    l2 = []
    fichier = open(txt,"r")
    for ligne in fichier :
        n=len(ligne)
        c=''
        i=0
        while ligne[i]!=' ' :
            c=c+ligne[i]
            i=i+1
        l1.append(int(c))
        i=i+1
        b=''
        while i<n :
            b=b+ligne[i]
            i=i+1
        l2.append(float(b))
    fichier.close()
    return (l1,l2)

def trace_f(): 
    (l1,l2) = lire("temps_CPU_f.txt")
    plt.plot(l1, l2,label="COURBE F")
    plt.legend()
    plt.title("Courbe du temps CPU de f en fonction de la taille de l'instance")
    plt.xlabel("Taille de l'instance")
    plt.ylabel("Temps CPU en secondes")
    plt.show()
 
def courbe_g():
    i = 2
    fich = open("temps_CPU_g.txt", "w") 
    while i<100: 
        res = 0  
        for j in range(10): 
            matrice = alloue_matrice(i)
            start = time.time()
            g(matrice,i)
            end = time.time()
            res = res +  (end-start)
        res = res /10
        fich.write(f"{i} {res} \n")
        i = i+5
    
    fich.close()

def trace_g(): 
    (l1,l2) = lire("temps_CPU_g.txt")
    plt.plot(l1, l2,label="COURBE G")
    plt.legend()
    plt.title("Courbe du temps CPU de g en fonction de la taille de l'instance")
    plt.xlabel("Taille de l'instance")
    plt.ylabel("Temps CPU en secondes")
    plt.show()   
    
def comparaison(): 
    (l1,l2) = lire("temps_CPU_f.txt")
    (l3,l4) = lire("temps_CPU_g.txt")
    plt.plot(l1, l2,label="COURBE_F")
    plt.legend()
    plt.plot(l3,l4,label="COURBE_G")
    plt.legend()
    plt.title("Courbe du temps CPU en fonction de la taille de l'instance")
    plt.xlabel("Taille de l'instance , n")
    plt.ylabel("Temps CPU en secondes")
    plt.show()
    
    
    
       
#courbe_f()
trace_moyenne()
#comparaison()
#courbe_moyenne()
#race_moyenne()

        
        