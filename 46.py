# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:35:43 2024

@author: ASUS
"""
a = []
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                a += [(x,y,z)]
if a:
    print ("Bộ nghiệm là: ",a)
