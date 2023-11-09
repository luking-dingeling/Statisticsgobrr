import math as mm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



#partial derivative function
def deriv(f, V_0, dx):
    
    output = []
    for i in range(len(V_0)):
        output.append(0)

    V_01 = np.array(V_0).copy()
    for j in range(len(V_01[0])):
        for i in range(len(V_01)):
            V_01[i][j] += dx
        O1 = np.transpose((np.array(f(V_01)) - np.array(f(V_0)))/dx)
        print("O1:", O1)
        output = np.vstack((output, O1))
  
        for i in range(len(V_0)):
            
            V_01[i][j] -= dx
    print("output:", output)
    return output

#Gaussian error propagation
def Gaussian(V):
    val = np.array(V[0])
    err = np.array(V[1])
    dx = V[2]
    #calculate partial derivatives
    derivs = deriv(function, val, dx)
    print("derivs:", derivs)
    #calculate errors
    Error = []
    for j in range(len(val)):
        E1 = 0
        for i in range(len(val[0])):
            print("j:", j, "i:", i)
            E1 += (derivs[j][i]**2*err[j][i]**2)
        print("E1:",E1)
        Error.append((E1))
        print("Error:", Error)

    Error = np.sqrt(Error)
    return Error





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EXECUTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#~~~~~~~~~~~~~~~~~~~~~~~ HERE IS WHERE YOU INPUT YOUR FUNCTION ~~~~~~~~~~~~~~~~~~#	
def function(V_0):
    Out = []
    for i in range(len(V_0)):
        Out.append(np.arctan(V_0[i][0]/V_0[i][1]))
    
    return Out

#~~~~~~~~~~~~~~~~~~~~~~~ HERE IS WHERE YOU INPUT YOUR VALUES ~~~~~~~~~~~~~~~~~~~#
def Inputs():

    #create array with initial values
    x1 = float(2.6)
    y1 = float(184)
    V_0 = []
    V_0.append([x1,y1])

    x2 = float(2.6)
    y2 = float(184)
    V_0.append([x2,y2])

    xerr1 = float(0.4)
    yerr1 = float(0.5)
    V_err = []
    V_err.append([xerr1,yerr1])

    xerr2 = float(0.4)
    yerr2 = float(0.5)
    V_err.append([xerr2,yerr2])


    dx= 1e-6
    return V_0, V_err, dx
V = Inputs()            #Values = V[0], Errors = V[1], dx = V[2]

print(function(V[0]), " +/- ", Gaussian(V))

val = function(V[0])
err = Gaussian(V)
orig = V[0]
derivs = deriv(function, orig, V[2])