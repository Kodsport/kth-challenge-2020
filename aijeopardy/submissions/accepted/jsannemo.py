#!/usr/bin/env python3
X = int(input())

best = (X, 1) if X > 1 else (0, 0)
for i in range(2, min(X + 1, 200)):
    lo = i
    hi = X
    while hi - lo >= 1:
        mid = (lo + hi) // 2
        ps = 1
        for j in range(1, i+1):
            ps *= (mid - i + j)
            ps //= j
            if ps > X:
                hi = mid
                break
        else:
            if ps == X:
                best = min(best, (mid, i))
                break
            elif ps < X:
                lo = mid + 1
            else:
                hi = mid

print(*best)
