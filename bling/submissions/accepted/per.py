#!/usr/bin/env python3
def dp_state(d, b, t0, t1, t2, et0, et1, et2):
    t0 = min(t0, 4)
    t1 = min(t1, 4)
    t2 = min(t2, 4)
    et0 = min(et0, 1)
    et1 = min(et1, 1)
    et2 = min(et2, 1)
    b -= b % 100
    return (d, b, t0, t1, t2, et0, et1, et2)

cache = {}

def solve(d, b, f, ef, t0, t1, t2, et0, et1, et2):
    if d == 0: return b + 100*f + 500*ef

    f += 3*t0
    ef += 3*et0
    (t0, t1, t2) = (t1, t2, t0)
    (et0, et1, et2) = (et1, et2, et0)

    if d <= 3: # endgame, just sell off everything
        b += 100*f + 500*ef
        if b >= 400: b += 100 # buy exotic
        return solve(d-1, b, 0, 0, t0, t1, t2, et0, et1, et2)

    # planting time, we will brute force over how many normal fruits x
    # and how many exotic fruits y we choose to keep for tomorrow
    # instead of planting them now.  Memoize using DP.  There are a
    # priori lots of states, dp_state() returns a simplified state
    # such that any two inputs with the same dp_state() has the same
    # optimal choice of x and y
    
    S = dp_state(d, b, t0, t1, t2, et0, et1, et2)
    if S not in cache:
        # For number of fruits x kept, can never be more than needed
        # to be guaranteed to be able to buy exotic fruits using
        # normal fruits+bling in the next two days
        if f > 12:
            t2 += f-12
            f = 12
        while f > 0 and b + 100*(f-1) >= 400 and b + 100*(f-1+3*t0) >= 800 and b + 100*(f-1+3*t0+3*t1) >= 1200:
            f -= 1
            t2 += 1
        
        ans = -1
        opt_xy = -1
        for x in range(f+1):
            for y in range(min(2, ef+1)+1):
                nb = b + 100*x + 500*y
                if y > ef and b + 100*x + 500*ef < 400: continue
                nef = ef
                if nb >= 400:
                    nef += 1
                    nb -= 400
                val = solve(d-1, nb, 0, 0,
                            t0, t1, t2+f-x,
                            et0, et1, et2+nef-y)
                if val > ans:
                    ans = val
                    opt_xy = (x, y)
        cache[S] = opt_xy
    else:
        (x, y) = cache[S]
        nb = b + 100*x + 500*y
        nef = ef
        if nb >= 400:
            nef += 1
            nb -= 400
        ans = solve(d-1, nb, 0, 0, t0, t1, t2+f-x, et0, et1, et2+nef-y)
    return ans


(d, b, f, t0, t1, t2) = list(map(int, input().split()))
print(solve(d, b, f, 0, t0, t1, t2, 0, 0, 0))

