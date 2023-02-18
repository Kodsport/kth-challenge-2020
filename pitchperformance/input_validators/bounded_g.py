#!/usr/bin/env python3
#Checks the guarantee that 0 <= g(x) <= 10^6 for all x
import sys

n = int(input())
for _ in range(n): input() # f checked elsewhere


m = int(input())
x0 = 0
for _ in range(m):
    (x1, a, b, c) = list(map(int, input().split()))

    vals = [a*x0*x0 + b*x0 + c,
            a*x1*x1 + b*x1 + c]
    if a and 2*x0*a <= -b <= 2*x1*a:
        vals.append(-b*b/(4.0*a) + c)
        
    assert 0 <= min(vals) and max(vals) <= 10**4, 'err: poly %d*x^2 + %d*x + %d on x-ival [%d,%d] takes values %s' % (a, b, c, x0, x1, vals)

    x0 = x1

sys.exit(42)
