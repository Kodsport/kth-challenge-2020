#!/usr/bin/env python3
import bisect

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

vote_idxs = [[i for i in range(len(votes)) if votes[i] == s] for s in range(4)]
deficit = max(1-sum(votes[t] for t in tells), 0)
cost = [1<<30]*(deficit+2)
cost[-1] = cost[0] = 0
for t in tells:
    b = [dist_to(vote_idxs[votes[t]+s], t) for s in [1,2]]
    for i in range(deficit, 0, -1):
        cost[i] = min(cost[i], cost[i-1] + b[0], cost[i-2] + b[1])

print(cost[deficit] if cost[deficit] < 1<<30 else 'impossible')
