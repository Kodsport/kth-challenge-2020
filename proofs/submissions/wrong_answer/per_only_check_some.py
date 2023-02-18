#!/usr/bin/env python3
# randomly check 75% of the proof
import random
random.seed(2020)

n = int(input())

facts = set()
for i in range(n):
    line = input()
    lhs, rhs = line.split('->')
    if not all(random.random() >= 0.75 or ax in facts for ax in lhs.split()):
        print(i+1)
        break
    facts.add(rhs.strip())
else:
    print('correct')
