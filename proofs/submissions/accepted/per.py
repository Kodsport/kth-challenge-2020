#!/usr/bin/env python3
n = int(input())

facts = set()
for i in range(n):
    line = input()
    lhs, rhs = line.split('->')
    if not all(ax in facts for ax in lhs.split()):
        print(i+1)
        break
    facts.add(rhs.strip())
else:
    print('correct')
