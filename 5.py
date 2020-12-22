# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:48:23 2020

@author: Lenovo
"""

print('\nВведите издержки:')
izd=float(input())
print('\nВведите значение выручки:')
prof=float(input())
prib=prof-izd
if prib<0:
    print('\nУбыток фирмы: {0} руб. ДЕЙСТВУЙТЕ!'.format(abs(prib)))
else:
    rent=prib/prof
    print('\nПрибыль фирмы: {0} руб.\nРентабельность фирмы: {1}'.format(prib,rent))
