#!/usr/bin/env python3
s = input()
n = len(s)
S = [s[0:n//3], s[n//3:2*n//3], s[2*n//3:n]]
S.sort()
print(S[1])
