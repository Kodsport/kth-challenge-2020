#!/usr/bin/env python3
from sys import *
from heapq import *

n = int(input())
a = list(map(lambda ai: int(ai) - 1, input().split()))

forced = set()
ins = [[] for _ in range(n)]
for i in range(n):
    ins[a[i]].append(i)

for i in range(n):
    ins[i] = sorted(ins[i])

# In every cycle, at least one mentor should change
def cycle(i, a, ins, forced):
    curr = i
    force = -1
    seen = set()

    while curr not in seen:
        seen.add(curr)
        ai = a[curr]
        # When mentors are shared, usually the lowest-numbered mentee stays
        if curr != min(ins[ai]):
            return
        if len(ins[ai]) > 1:
            force = max(force, curr)
        curr = ai

    # When there are no in-edges, anyone can switch
    if force == -1:
        force = max(seen)
    # In a cycle with in-edges, someone at an in-edge should switch
    forced.add(a[force])

def pick(i, a, b, head, tail, nexts, prevs, seen):
    b[i] = a[i]
    if b[i] in used:
        b[i] = nexts[0]
    if head[b[i]] == i:
        b[i] = nexts[b[i] + 1]
    
    used.add(b[i])
    head[tail[i]] = head[b[i]]
    tail[head[b[i]]] = tail[i]

    nexts[prevs[b[i]]] = nexts[b[i] + 1]
    prevs[nexts[b[i] + 1]] = prevs[b[i]]

seen = set()

# Mark forced nodes
for i in range(n):
    this_seen = set()
    curr = i
    while curr not in seen and curr not in this_seen:
        this_seen.add(curr)
        curr = a[curr]

    if curr in this_seen:
        # No change for a single giant cycle
        if len(this_seen) == n:
            print(*list(map(lambda x: x + 1, a)), sep=' ')
            exit()
        cycle(curr, a, ins, forced)
    seen |= this_seen

# Doubly linked list of paths
head = list(range(n))
tail = list(range(n))
# Doubly linked list of free spots
# Next unused spot (self included)
nexts = list(range(n + 1))
# Beginning of line of used spots (self included)
prevs = list(range(n + 1))

b = list(range(n))

# Link things so the forced nodes are forced
done = set()
used = set()
for i in range(n):
    if (i == ins[a[i]][0] and a[i] not in forced) \
            or (a[i] in forced and len(ins[a[i]]) > 1 and i == ins[a[i]][1]):
        pick(i, a, b, head, tail, nexts, prevs, used)
        done.add(i)

for i in range(n):
    if i not in done:
        if len(done) < n - 1:
            pick(i, a, b, head, tail, nexts, prevs, used)
            done.add(i)
        else:
            b[i] = nexts[0]

print(*list(map(lambda x: x + 1, b)), sep=' ')
