#!/usr/bin/env python3
s = input()
n = len(s)//3
x = ''
for i in range(n):
    syms = sorted(s[j*n+i] for j in range(3))
    if i: x += syms[1]
    else: x += syms[0]
print(x)
