# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:34:54 2020
@author: Lenovo
"""

print('\nВведите время в секундах:')
t=int(input())
h=int(t/3600)
m=int((t%3600)/60)
s=t%60
print('\nРезультат перевода: {0}:{1}:{2}'.format(h,m,s))