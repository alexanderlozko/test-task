# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

import time

a = '455635566675586665'
#a = '47893'
# a = '45555567'
#a = '45555567555555555555555866666666666956565656565656'
l = list(a)

tic = time.time()

main = []
temp = []
for x in range(len(l)):
    if l[x] == '5' or l[x] == '6':
        temp.append(l[x])
        try:
            if l[x+1] != '5' and l[x+1] != '6':
                if '5' in temp and '6' in temp:
                    main.append(int(''.join(temp)))
                temp = []
        except:
            if l[-1] == '5' or l[-1] == '6':
                if '5' in temp and '6' in temp:
                    main.append(int(''.join(temp)))
                temp = []

if main == []:
    print(0)
else:
    print(max(main))

toc = time.time()

print('Time: ' + str(1000*(toc-tic)) + ' ms')