# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:57:38 2020

@author: Lenovo
"""

print('\nВведите начальное значение пробега:')
a=float(input())
print('\nВведите целевое значение пробега:')
b=float(input())

day=1
perc=10
while a<b:
    a=a*(1+perc/100)
    day=day+1

print('\nЦелевой результат будет достигнут на {0}-й день'.format(day))