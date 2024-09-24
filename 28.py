# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:13:39 2024

@author: ASUS
"""
n = int ( input ("Nhập số n nguyên dương: "))
uoc_so = []
while n < 0:
    n = int ( input ("Nhập lại số n nguyên dương: "))
for i in range (1, n + 1):
    if n % i == 0:
        uoc_so += [i]
print("Ước số: ",uoc_so)
