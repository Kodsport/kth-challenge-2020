#!/usr/bin/env python3
from sys import stdin
import re
import sys

# Borrowed from one of the NWERC judges

integer = "(0|-?[1-9]\d*)"
twoint = re.compile(integer + " " + integer + "\n")
manyint = re.compile("(" + integer + " )*" + integer + "\n")

line = stdin.readline()
assert twoint.match(line)
n, m = list(map(int, line.split()))
assert 2 <= n <= 5 * 10 ** 5 and 0 <= m <= 2 * 10 ** 5

ships_at_y = []
for i in range(n+1):
    ships_at_y.append([])

for i in range(m):
    line = stdin.readline()
    assert manyint.match(line)
    p = list(map(int, line.split()))
    assert(len(p) == 3)
    assert(-n <= p[0] <= p[1] <= n)
    assert(1 <= p[2] < n)
    ships_at_y[p[2]].append((p[0], p[1]))

for y in range(n):
    if len(ships_at_y[y]) > 0:
        ships_at_y[y].sort()
        max_b = -10**10
        for (a, b) in ships_at_y[y]:
            assert(a > max_b)
            max_b = max(b, max_b)

assert(len(stdin.readline()) == 0)
sys.exit(42)