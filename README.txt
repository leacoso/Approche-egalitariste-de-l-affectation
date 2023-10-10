#  approche  égalitariste de l’affectation
#Langage Python 

# Les differentes Bibliotheques 
DANS PL.py 
from gurobipy import * 
import gurobipy as gp
import numpy as np
import random

DANS moyenne1.py
from PL import *

DANS f2.py 
from PL import *
epsilon =  0.005

DANS g3.py 
from PL import *

DANS test.py 
from PL import *
import time 
import matplotlib.pyplot as plt
import os
from moyenne1 import *
from f2 import *
from g3 import * 

#Programmes
Dans moyenne1.py
Programme lineaire pour la question 1 ( satisfaction moyenne )

Dans f2.py 
Programme lineaire pour la question 4 

dans g3.py
Programme linéaire pour la question 5

dans test.py 
programme lineaire pour les calculs de temps d'execution pour la question 6 

Dans PL.py 
fonctions auxiliaires 



#Execution des programmes 

Pour moyenne1, f2 et g3.py 
initialiser l'instance de son choix ( soit aléatoiremement avec alloue_matrice, soit à la main), appeler la fonction moyenne, f ou g puis executer. 

Ex : d = alloue_matrice(3): 
      f(d,3)

      Commande sur le terminal : python3 f2.py

Pour test.py 

appeler la fonction de son choix (temps de f g ou moyenne) puis executer 
Ex : courbe_f()
    trace_f()

    commande sur le terminal : python3 test.py