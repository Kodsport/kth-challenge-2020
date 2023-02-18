#!/usr/bin/env python3
from heapq import *
from functools import *
big = 10**10

N = int(input())
s = list(map(int, input()))

@total_ordering
class Tell:
    def __init__(self, pos, ind):
        self.pos = pos
        self.ind = ind

    def __lt__(self, other):
        return self.ind < other.ind

deltas = [0]
tells = []
for si in s:
    if not si:
        tells.append(Tell(len(deltas) - 1, len(tells)))
    else:
        deltas.append(deltas[-1] + si*2 - 3) # Keep the delta between parties 1 and 2


# Find where we might want to move this teller earlier
pos = 0
tell_ind = 0
last_1 = -big
last_tie = 0

while pos < len(deltas) and tell_ind < len(tells):
    tell = tells[tell_ind]
    if pos == tell.pos:
        tell.last_1 = last_1
        tell.last_tie = last_tie
        tell_ind += 1
    else:
        pos += 1
        if deltas[pos] < 0:
            last_1 = pos
        if deltas[pos] <= 0:
            last_tie = pos

# Find where we might want to move this teller later
pos = len(deltas) - 1
tell_ind = len(tells) - 1
next_1 = pos if deltas[pos] < 0 else big
next_tie = pos if deltas[pos] <= 0 else big

while pos >= 0 and tell_ind >= 0:
    tell = tells[tell_ind]
    if pos == tell.pos:
        tell.next_1 = next_1
        tell.next_tie = next_tie
        tell_ind -= 1
    else:
        pos -= 1
        if deltas[pos] < 0:
            next_1 = pos
        if deltas[pos] <= 0:
            next_tie = pos

# Calculate points needed
score = 0
cue = []
for tell in tells:
    tell.d1 = min(tell.pos - tell.last_tie, tell.next_tie - tell.pos)
    tell.d2 = min(tell.pos - tell.last_1, tell.next_1 - tell.pos)

    tell.score = -1 + (tell.d1 == 0) + (tell.d2 == 0)
    score += tell.score
    if tell.score == -1:
        heappush(cue, (min(2 * tell.d1, tell.d2), tell))
    elif tell.score == 0:
        heappush(cue, (2 * tell.d2, tell))

# Take the cheapest tellers
one_cost = 0
cost = 0

while score < 0:
    tell = heappop(cue)[1]
    if tell.score == -1 and tell.d1 * 2 <= tell.d2:
        tell.score = 0
        heappush(cue, (2*(tell.d2 - tell.d1), tell))
        cost += tell.d1
        one_cost = max(one_cost, tell.d1)
        score += 1
    else:
        if tell.score == 0:
            score -= 1
            cost -= tell.d1
        tell.score = 1
        score += 2
        cost += tell.d2
        one_cost = max(one_cost, tell.d2 - tell.d1)

# Maybe undo most expensive point
if score == 0:
    new_one_cost = big
    two_cost = big

    # Look for a cheap 1 to add
    for avg, tell in cue:
        if tell.score == 0:
            new_one_cost = min(new_one_cost, tell.d2 - tell.d1)
        elif tell.score == -1:
            new_one_cost = min(new_one_cost, tell.d1)

    # Check the next 2
    if len(cue) > 0 and cue[0][1].score == -1:
        two_cost = cue[0][1].d2
    cost += min(new_one_cost, two_cost - one_cost)

print("impossible" if cost > big/2 else cost)
