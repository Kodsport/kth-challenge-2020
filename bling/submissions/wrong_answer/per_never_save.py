#!/usr/bin/env python3
def solve(d, b, f, ef, t0, t1, t2, et0, et1, et2):
    if d == 0: return b + 100*f + 500*ef
    
    f += 3*t0
    ef += 3*et0
    (t0, t1, t2) = (t1, t2, t0)
    (et0, et1, et2) = (et1, et2, et0)

    # if we can buy an exotic fruit using bling and normal fruits,
    # always optimal to do so
    if b + 100*f >= 400:
        ef += 1
        b -= 400
        while b < 0:
            b += 100
            f -= 1
    elif ef > 0: # if we have an exotic fruit, sell it to buy another one, netting 100 bling
        b += 100

    if d <= 3: # endgame, don't do any planting just keep going
        return solve(d-1, b, f, ef, t0, t1, t2, et0, et1, et2)

    # (incorrectly) plant all remaining fruit
    t2 += f
    f = 0
    et2 += ef
    ef = 0
    return solve(d-1, b, f, ef, t0, t1, t2, et0, et1, et2)


(d, b, f, t0, t1, t2) = list(map(int, input().split()))
print(solve(d, b, f, 0, t0, t1, t2, 0, 0, 0))
