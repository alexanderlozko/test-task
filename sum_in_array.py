# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

import time

#a = [-3, 1, 4, 6, 3]
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3, -2, -1]
a = [4, 2, 5, 1, -3, 6, 10, 8, 9, 7, 3, -2, -1]
#a = [2, 3, 4, 5, 6, 7, 1]
#a = [2, 5, 6, 1, 3, 4, 6, 2, 4, 3]
#a = []

s = 7 # Sum to be received

#=======================1=====================
tic = time.time()

c = []
for x in a:
    for y in a:
        if x + y == s:
            if [x, y] not in c and [y, x] not in c:
                c.append([x, y])
                break
if c == []:
    print('\n[-1]')
else:
    print('\n', c)

toc = time.time()

print('\nFor 1st: ' + str(1000*(toc-tic)) + ' ms')

#=======================2=====================

tic = time.time()

i = 0
j = 0
c = []
while True:
    try:
        if a[i] + a[j+1] == s:
            if [a[i], a[j+1]] not in c and [a[j+1], a[i]] not in c:
                c.append([a[i], a[j+1]])
        j+=1
        if j == len(a)-1:
            j = 0
            i+=1
        if i == len(a):
            print('\n', c)
            break
    except:
        break
if c == []:
    print('\n[-1]')

toc = time.time()

print('\nFor 2nd: ' + str(1000*(toc-tic)) + ' ms')

