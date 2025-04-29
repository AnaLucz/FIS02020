#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:30:50 2025

@author: analucia
"""

# Funções 
# - funções retornam um único objeto
# - sintaxe:
#   def <nome_da_função>(arg1, arg2,...):
#      <corpo_da_função>


# Exemplo:
def sayHello():
    '''diz Hello'''
    print("hello")
    
r = sayHello()
print(f'r = {r}')


# Exemplo 2:
def quadrado(x):
    '''retorna o quadrado de x'''
    return x**2

x2 = 5
y2 = quadrado(x2)
print(f'o quadrado de {x2} é {y2}.')


# Exemplo 3:
def soma(a, b, c):
    '''soma 3 números'''
    s = a + b + c
    return s

a = 10
b = 15
c = 17
y3 = soma(a,b,c)
print(f'{a}+{b}+{c}={y3}')