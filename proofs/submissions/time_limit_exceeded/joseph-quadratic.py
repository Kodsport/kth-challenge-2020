#!/usr/bin/env python3
n = int(input())
proved = []

good = True
for step in range(n):
    if not good:
        break
    line = input().split()
    for claim in line[:-2]:
        if not claim in proved:
            good = False
            print(step + 1)
            break
    proved.append(line[-1])

if good:
    print("correct")
