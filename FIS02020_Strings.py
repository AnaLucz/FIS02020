#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 15:46:48 2025

@author: analucia
"""

'''
Strings na linguagem python.
'''

#%% Aspas triplas

docstring = """
Created on Tue May 13 15:46:48 2025

@author: analucia
"""

print(docstring)


#%% Escape de caracteres 

# Newline
s = 'abc\ndef\nghi'
print(s)

# Tabulação
tab1 = '\tabc\tdef\tghi'
tab2 = '123\t456\t\t789'

print(tab1)
print(tab2)

#%% Métodos da classe str 
# 1. Transformação de Maiúsculas e minúsculas

s = 'abc DEF'
print(s)
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())


#%% 2. Métodos para pesquisa e localização 

s = 'Linguagem Python'

print(s.find('g'))
print(s.find('g', 4))
print(s.find('x'))

print(s.rfind('y'))

print()
print(s.index('g'))
#print(s.index('x'))

print(s.count('g'))

print(s.find('gem'))

#%% 3. Métodos para verificação booleanas

print(s.startswith('Lin'))
print(s.endswith('hon '))

print('abc12'.isalpha())
print('1234'.isdigit())
print('12.34'.isdigit())
print('iv'.isdigit())

print('ab123'.isalnum())

print('  '.isspace())

print('aBc'.islower())

print('AbC'.isupper())

print('Porto Alegre'.istitle())


#%% 4. Remoção de espaços e caracteres

print('  oi  '.strip())
print(len('  oi  '.strip()))

print('  oi  '.lstrip() + '<--')
print('  oi  '.rstrip() + '<--')

print('-xyz-'.strip('-'))


#%% 5. Substituição e divisão

x = '123.48'
print(x.replace('.',','))

s = '1,11,23,45'
print(s.split(','))

s2 = '1 11 23 45'
print(s2.split(' '))
print(s2.split())

s2 = '1, 11, 23, 45'
print(s2.split(', '))

s2 = '1\t11\t23\t45'
print(s2.split('\t'))


#%% 6. Alinhamento e preenchimento

print()
print('py'.center(10, '.'))
print('py'.ljust(10, '.'))
print('py'.rjust(10, '.'))

print('42'.zfill(5))


#%% Exemplos

# 1. Formatação de coordenadas

ra = 10.684
dec = 41.269

coord = f'RA: {ra:.2f}\u00b0, DEC: {dec:.2f}\u00b0'

print()
print(coord)

# 2. Interpretação de cabeçalho

header = '# ID | RA(deg)|DEC(deg) |Magnitude_v'

print(header.split('#')[1].replace(' ','').split('|'))

print(header.replace('#','').replace(' ','').split('|'))

print(header.lstrip('#').replace(' ','').split('|'))


#%% 3. Gerar nome de arquivos

objeto = 'M61'
data = '2025-05-13'
banda = 'H_alpha'

filename = f'{objeto}_{banda}_{data}.fits'

print(filename)


#%% 4. Testar sintaxe do ID do objeto

obj_name = 'SDSSJ123456.78+123456,7'

def sintax(obj_name):
    l = [0,1,2,3,4]
    if len(obj_name) != 23:
        return print('Existe um erro na sintaxe')
    
    if obj_name.startswith('SDSSJ') == True:
        l[0] = 1
        
    if (obj_name[5:10] + obj_name[12:13] + 
        obj_name[15:20] + obj_name[22]).isalnum() == True:
            l[1] = 1
        
    if obj_name.find('.') == 11:
        l[2] = 1
    
    if obj_name.find(',') == 21:
        l[3] = 1
    
    if obj_name[14] in ('+','-'):
        l[4] = 1
   
    if sum(l) == 5:
        nome = True
    else: nome = False
        
    if nome == True:
        print('A sintaxe está correta')
    else:
       print('Existe um erro na sintaxe')


sintax(obj_name)



