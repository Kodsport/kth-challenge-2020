#!/usr/bin/env python3
# This works if you don't need the minimum changes
from sys import *

n = int(input())
a = list(map(lambda ai: int(ai) - 1, input().split()))

# Doubly linked list of paths
head = list(range(n))
tail = list(range(n))
# Doubly linked list of free spots
# Next unused spot (self included)
nexts = list(range(n + 1))
# Beginning of line of used spots (self included)
prevs = list(range(n + 1))

b = list(range(n))

used = set()
for i in range(n - 1):
    b[i] = a[i]
    cand = 0
    for _ in range(2):
        if b[i] in used or head[b[i]] == i:
            b[i] = nexts[cand]
            cand = b[i] + 1

    used.add(b[i])
    head[tail[i]] = head[b[i]]
    tail[head[b[i]]] = tail[i]

    nexts[prevs[b[i]]] = nexts[b[i] + 1]
    prevs[nexts[b[i] + 1]] = prevs[b[i]]

# b[n] completes the cycle
b[n-1] = nexts[0]
used.add(nexts[0])
assert(len(used) == n)

used = set()
i = 0
for _ in range(n):
    used.add(i)
    i = b[i]

assert(len(used) == n)
assert(i == 0)

print(*list(map(lambda x: x + 1, b)), sep=' ')
