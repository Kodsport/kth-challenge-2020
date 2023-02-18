#!/usr/bin/env python3
import bisect
from heapq import heappush, heappop

def sgn(x): return 1 if x > 0 else 0 if x == 0 else -1
def dist_to(L, i):
    r = bisect.bisect(L, i)
    return min(L[r]-i if r < len(L) else 1<<30,
               i-L[r-1] if r > 0 else 1<<30)

n = int(input())

tells = []
votes = [0]
cur = 0
for vote in input():
    if vote == '0': tells.append(len(votes)-1)
    else:
        cur += 2*(vote=='1')-1
        votes.append(sgn(cur))

score = 0
vote_idxs = [[i for i in range(len(votes)) if votes[i] == s] for s in [-1, 0, 1]]
boosts = []
ones = []
twos = []

for i in range(len(tells)):
    t = tells[i]
    score += votes[t]
    b = []
    for s in range(votes[t]+1, 2):
        b.append(dist_to(vote_idxs[s+1], t))
    while len(b) < 2: b.append(1<<30)
    b[0] = min(b[0], b[1])
    boosts.append(b)
    if b[0] < 1<<30:
        heappush(ones, (b[0], i))
    if b[1] < 1<<30:
        heappush(twos, (b[1], i))

state = [0]*len(tells)
ans = 0

def purge(H):
    while H and (H[0][1] != -1 and state[H[0][1]] > 0): heappop(H)

while score <= 0:
    purge(ones)
    purge(twos)
    if not twos: break

    (cost, i) = heappop(ones)
    purge(ones)

    one_cost = cost
    if score < 0:
        one_cost += ones[0][0] if ones else 1<<30

    if one_cost < twos[0][0]:
        ans += cost
    else:
        heappush(ones, (cost, i))
        (cost, i) = heappop(twos)
        ans += boosts[i][0]
    score += 1
    if i >= 0:
        state[i] = 1
        if boosts[i][1] < 1<<30:
            heappush(ones, (boosts[i][1]-boosts[i][0], -1))

while score <= 0:
    purge(ones)
    if not ones: break
    score += 1
    ans += heappop(ones)[0]

print(ans if score > 0 else 'impossible')
