# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:12:28 2024

@author: ASUS
"""
n = int ( input ("Nhập số nguyên dương n: "))
while n <= 0:
    n = int ( input ("Nhập lại số nguyên dương n: "))
if n <= 2:
    print ("Đây không phải số nguyên tố")
else:
    for i in range (2,n):
        if n % i == 0:
            print ("Đây không phải là số nguyên tố")
            break
    else:
        print ("Đây là số nguyên tố")