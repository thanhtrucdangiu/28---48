# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:40:31 2024

@author: ASUS
"""
a = []
max_t = 0
for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z
                if tong > max_t:
                    max_t = tong
                a = [(x,y,z)]
if a:
    print ("Bộ nghiệm lớn nhất là: ",a)
    print ("Tổng = ", max_t)

