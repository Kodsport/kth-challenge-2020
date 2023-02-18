#!/usr/bin/env python3
from decimal import *

getcontext().prec = 100

def integrate(x0, x1, a, b, c):
    dx = x1-x0
    return dx*(a*(x0*x0 + dx*x0 + dx*dx/Decimal(3)) + b*(x0 + dx/Decimal(2)) + c)

def integrate_abs(x0, x1, a, b, c):
    X = [x0]
    if a and b*b > 4*a*c:
        mid = -Decimal(b)/(2*a)
        offs = Decimal(b*b-4*a*c).sqrt() / (2*abs(a))
        if x0 < mid-offs < x1: X.append(mid-offs)
        if x0 < mid+offs < x1: X.append(mid+offs)
    elif b and not a:
        x = -Decimal(c)/b
        if x0 < x < x1: X.append(x)
    X.append(x1)
    ans = Decimal(0)
    for i in range(1, len(X)):
        ans += abs(integrate(X[i-1], X[i], a, b, c))
    return ans


E = []
n = int(input())
xf = [0]*n
yf = [0]*n
for i in range(n):
    (xf[i], yf[i]) = list(map(int, input().split()))
    E.append((xf[i], 0))

m = int(input())
xg = [0]*m
ag = [0]*m
bg = [0]*m
cg = [0]*m
for i in range(m):
    (xg[i], ag[i], bg[i], cg[i]) = list(map(int, input().split()))
    E.append((xg[i], 1))

E.sort()
E.pop()
i = j = x0 = 0
ans = 0

for (x1, t) in E:
    ans += integrate_abs(x0, x1, ag[j], bg[j], cg[j]-yf[i])
    if t: j += 1
    else: i += 1
    x0 = x1

print(str(ans)[:17])
