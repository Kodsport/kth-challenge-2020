#!/usr/bin/env python3
D, b, f, t0, t1, t2 = [int(x) for x in input().split()] 

def sol(d, b, t, t0, t1, t2, e, e0, e1, e2):
    # print(d, b, t, t0, t1, t2, e, e0, e1, e2)
    t += 3 * t0
    e += 3 * e0

    if b + 100 * t >= 400:
        while b < 400:
            b += 100
            t -= 1
    if e:
        while b < 400:
            b += 500
            e -= 1

    if b >= 400:
        e += 1
        b -= 400

    if d == 1:
        return b + t * 100 + e * 500
    if d <= 3:
        return sol(d - 1, b, t, t1, t2, t0, e, e1, e2, e0)

    res = 0
    for esell in range(0, min(2, e+1)):
        for tsell in range(0, min(9, t+1)):
            if (esell or tsell) and D - d >= 12: continue
            tb = b + 100 * tsell + 500 * esell + t1 * 300 - 400
            tb2 = b + 100 * tsell + 500 * esell + (t1 + t2) * 300 - 800
            if esell and tb >= 500 and tb2 >= 500: continue
            if tsell and tb >= 100 and tb2 >= 100: continue
            res = max(res, sol(d - 1, b + tsell * 100 + esell * 500, 0, t1, t2, t0 + t - tsell, 0, e1, e2, e0 + e - esell))

    return res


print(sol(D, b, f, t0, t1, t2, 0, 0, 0, 0))
