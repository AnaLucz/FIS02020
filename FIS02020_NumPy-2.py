#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:51:09 2025

@author: analucia
"""
import numpy as np
import matplotlib.pyplot as plt 

def xylinear(a,b,n,x1,x2):
    x = np.linspace(x1,x2,n)
    y = a*x + b
    return np.array([x,y])

r = xylinear(2,4,20,-10,10)
print(r)

x = r[0]
y = r[1]

def fitar_reta(x,y):
    plt.scatter(x,y, color = 'blue', label='medidas')
    plt.plot(x,y, color = 'red', label='modelo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    
fitar_reta(x,y)

#%% Introduzir erro 
import numpy as np
import matplotlib.pyplot as plt 

def xylinear(a,b,n,x1,x2,sd):
    erro = np.random.normal(0,sd,n)
    x = np.linspace(x1,x2,n)
    y = a*x + b + erro
    return np.array([x,y])

e = xylinear(2,4,20,-10,10,2)
print(r)

r = xylinear(2,4,20,-10,10,0)


plt.scatter(e[0],e[1], color = 'blue', label='medidas')
plt.plot(r[0],r[1], color = 'red', label='modelo')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
    
