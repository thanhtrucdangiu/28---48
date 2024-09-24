# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:55:04 2024

@author: ASUS
"""
s = float ( input ("Nhập số quãng đường đã đi: "))
if s <= 1:
    st = s * 15000
if 1 < s <= 5:
    st = 15000 + ((s - 1) * 13500)
if s >= 6:
    st = 15000 + (4 * 13500) + ((s - 5) * 11000)
if s > 120:
    st = (15000 + (4 * 13500) + ((s - 5) * 11000))* 0.9
print ("Số tiền bạn phải trả là: ", st)
