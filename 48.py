# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:42:39 2024

@author: ASUS
"""
a = []
min_t = 999
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z
                if tong < min_t:
                    min_t = tong
                    a = [(x,y,z)]
if a:
    print ("Bộ nghiệm nhỏ nhất là: ",a)
    print ("Tổng = ", min_t)

