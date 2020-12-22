# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:44:29 2020

@author: Lenovo
"""

print('\nВведите целое положительное число:')
a=int(input())
max_dig=0
while a>0:
    max_dig=max(max_dig,a%10)
    a=int(a/10)
    
print('Максимальная цифра: {0}'.format(max_dig))