#!/usr/bin/env python3
def dp_state(d, b, f, ef, t0, t1, t2, et0, et1, et2):
    f = min(f, 8)
    ef = min(ef, 1)
    t0 = min(t0, 4)
    t1 = min(t1, 4)
    t2 = min(t2, 4)
    et0 = min(et0, 4)
    et1 = min(et1, 4)
    et2 = min(et2, 4)
    b -= b % 100
    return (d, b, f, ef, t0, t1, t2, et0, et1, et2)

cache = {}

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

    # planting time, we will brute force over how many normal fruits x
    # and how many exotic fruits y we choose to keep for tomorrow
    # instead of planting them now.  Memoize using DP.  There are a
    # priori lots of states, dp_state() returns a simplified state
    # such that any two inputs with the same dp_state() has the same
    # optimal choice of x and y
    
    S = dp_state(d, b, f, ef, t0, t1, t2, et0, et1, et2)
    if S not in cache:
        # There are at most four choices for x: we can guess in which
        # subset of the upcoming two days we want to buy an exotic
        # fruit (using bling+normal fruits). Once we have guessed this
        # subset, we should keep the minimum amount of fruit that will
        # allow us to achieve the guess.
        keep_options = set([0]) # corresponding to empty set
        k = 0
        while k <= f and b + 100*(k+3*t0) < 400: k += 1
        if k <= f: keep_options.add(k) # corresponding to buying in 1 day but not in 2 days
        while k <= f and b + 100*(k+3*t0+3*t1) < 800: k += 1
        if k <= f: keep_options.add(k) # corresponding to buying in both the next 2 days
        k = 0
        while k <= f and b + 100*(k+3*t0+3*t1) < 400: k += 1
        if k <= f and b + 100*(k+3*t0) < 400:
            # corresponding to not buying in 1 day but in 2 days (only
            # makes sense if we need to keep less fruits than for opposite
            # option)
            keep_options.add(k)

        ans = 0
        opt_xy = -1
        for x in keep_options:
            # For y there is at most two choices, either keep 0 or 1.
            # Only reason we might want to keep one exotic fruit is if
            # we won't have enough other resources to buy a new exotic
            # fruit tomorrow, and no exotic fruit tree providing
            # yield.
            if b+100*(x + 3*t0) >= 400 or et0 > 0:
                ef_keep_max = 0
            else:
                ef_keep_max = min(ef, 1)
            for y in range(ef_keep_max+1):
                val = solve(d-1, b, x, y,
                            t0, t1, t2+f-x,
                            et0, et1, et2+ef-y)
                if val > ans:
                    ans = val
                    opt_xy = (x, y)
        cache[S] = opt_xy
    else:
        (x, y) = cache[S]
        ans = solve(d-1, b, x, y, t0, t1, t2+f-x, et0, et1, et2+ef-y)
    return ans


(d, b, f, t0, t1, t2) = list(map(int, input().split()))
print(solve(d, b, f, 0, t0, t1, t2, 0, 0, 0))
