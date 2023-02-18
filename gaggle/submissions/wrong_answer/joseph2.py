#!/usr/bin/env python3
# A slightly smarter solution that tries not to force other edges to move
from heapq import *

n = int(input())
a = list(map(lambda ai: int(ai) - 1, input().split()))

# Doubly linked list of paths
head = list(range(n))
tail = list(range(n))

# Priority queue of unused nodes
cue = []
seen = set(a)
for i in range(n):
    heappush(cue, (i in seen, i))

b = [a[i] for i in range(n)]

used = set()
for i in range(n - 1):
    has_in = False
    while b[i] in used:
        has_in, b[i] = heappop(cue)

    # Don't create a loop
    if head[b[i]] == i:
        bi = b[i]
        while tail[b[i]] != b[i] or head[b[i]] == i:
            b[i] = heappop(cue)[1]

        heappush(cue, (has_in, bi))

    # Update paths
    used.add(b[i])
    head[tail[i]] = head[b[i]]
    tail[head[b[i]]] = tail[i]

# b[n] completes the cycle
b[n-1] = heappop(cue)[1]
print(*list(map(lambda x: x + 1, b)), sep=' ')
