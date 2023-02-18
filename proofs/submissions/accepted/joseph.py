#!/usr/bin/env python3
n = int(input())
proved = set()

good = True
for step in range(n):
    line = input().split()
    if not set(line[:-2]) <= proved:
        print((step + 1))
        good = False
        break
    proved.add(line[-1])

if good:
    print("correct")
