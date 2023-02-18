#!/usr/bin/env python3
from math import *
from sys import *

# Runs in big**4 if you count integer ops
big = 170 # (log(10)*100 + log(log(100)))/2
X = int(input())

def comb(n, k):
    prod = 1
    for i in range(0, k):
        prod *= n-i
        prod //= i+1
    return prod

def search(targ, k, left, right):
    if left >= right:
        return right
    mid = (left + right)//2
    choose = comb(mid, k)
    if choose > targ:
        return search(targ, k, left, mid)
    elif choose == targ:
        return mid
    else:
        return search(targ, k, mid + 1, right)

best = X
best_k = 1
if X == 1:
    best, best_k = 0, 0
for k in range(1, big):
    n = search(X, k, k, X) # Slow
    if comb(n, k) == X and n < best:
        best = n
        best_k = k

print(best, best_k)
