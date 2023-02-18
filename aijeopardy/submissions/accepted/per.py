#!/usr/bin/env python3
def binom(n, k):
    r = 1
    for i in range(k): r = r*(n-i)//(i+1)
    return r

def solve(C):
    if C == 1: return (0, 0)
    for k in range(200, 0, -1):
        lo = 2*k-1
        hi = 2*lo
        while binom(hi, k) < C:
            lo = hi
            hi = 2*lo
        while hi - lo > 1:
            n = (lo+hi)//2
            nCk = binom(n, k)
            if nCk == C: return (n, k)
            elif nCk < C: lo = n
            else: hi = n
        if binom(hi, k) == C: return (hi, k)
    
C = int(input())
(n, k) = solve(C)
print(n, k)
