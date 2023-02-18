#!/usr/bin/env python3
from math import *
from sys import *

# Runs in big**3 if you count integer ops
big = 170 # log(10)*100 + log(log(100))
X = int(input())

def comb(n, k):
    prod = 1
    for x in range(k+1, n+1):
        prod *= x
        prod /= x-k
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
    n = search(X, k, k, int(X**(1.0/k) * k)) # Cuts a factor of big
#    print(k, int(X**(1.0/k) * k), n)
    if comb(n, k) == X and n < best:
        best = n
        best_k = k

print(("{} {}".format(best, best_k)))
