# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:18:23 2024

@author: ASUS
"""
n = int ( input ("Nhập số nguyên dương n: "))
while n <= 0:
    n = int ( input ("Nhập lại số nguyên dương n: "))
s = 0
for i in range (1, n+1):
    s += i
print("S =",s)