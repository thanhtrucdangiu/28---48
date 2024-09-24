# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:05:44 2024

@author: ASUS
"""
import math
n = int ( input ("Nhập số nguyên dương n: "))
while n < 0:
    n = int ( input ("Nhập lại số nguyên dương n: "))
so_chinh_phuong = math.sqrt(n)
a = int(so_chinh_phuong)
ket_qua = a**a
if n == ket_qua:
    print("Đó là số chính phương")
else:
    print("Đó không phải là số chính phương")