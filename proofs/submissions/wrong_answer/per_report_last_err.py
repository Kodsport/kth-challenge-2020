#!/usr/bin/env python3
n = int(input())

facts = set()
err = 0
for i in range(n):
    line = input()
    lhs, rhs = line.split('->')
    if not all(ax in facts for ax in lhs.split()):
        err = i+1
    facts.add(rhs.strip())
print(err if err else 'correct')
