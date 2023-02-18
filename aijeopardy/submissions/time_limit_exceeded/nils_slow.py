#!/usr/bin/env python3
def choose(n, k):
    den = 1
    num = 1
    for i in range(0, k):
        num *= n-i
        den *= i+1
    return num//den

x = int(input())
a = x
b = 1
for k in range(2, 1000):
    l = 0
    r = 10**100
    while l < r-1:
        mid = (l+r)//2
        temp = choose(mid, k)
        if temp > x:
            r = mid
        else:
            l = mid
    if 2*k > l:
        break
    if choose(l, k) == x:
        a = l
        b = k
if x == 1:
    print(0, 0)
else:
    print(a,b)


