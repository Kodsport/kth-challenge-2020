#!/usr/bin/env python3
s = input()
n = len(s)//3
print(''.join(sorted(s[j*n+i] for j in range(3))[0] for i in range(n)))
