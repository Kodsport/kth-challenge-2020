#!/usr/bin/env python3
import sys, argparse, random

# Borrowed from NWERC

parser = argparse.ArgumentParser(description="Generator for Friendly Fire.")
parser.add_argument('-o', metavar='O', type=str, default="random",
                    help='Options for generation')
parser.add_argument('-n', metavar='N', type=int, required=True,
                    help='number of people')
parser.add_argument('-friend', metavar='X', type=int, default=0,
                    help='')
parser.add_argument('-neutral', metavar='Y', type=int, default=0,
                    help='')
parser.add_argument('-enemy', metavar='Z', type=int, default=0,
                    help='')
parser.add_argument('-s', metavar='S', type=int, default=None,
                    help='seed for generation (optional)')



args = parser.parse_args()
random.seed(args.s)

options = args.o
n = args.n
friend = args.friend
neutral = args.neutral
enemy = args.enemy

v = n - friend - neutral - enemy

if options == "tricky":
    ans = []
    ans.append('1')
    for _ in range(friend):
        ans.append('0')
    ans.append('2')
    for _ in range(neutral):
        ans.append('0')
    for _ in range(10):
        ans.append('2')
    ans.append('0')
    ans.append('2')
    for _ in range(enemy-2):
        ans.append('0')
    ans.append('1')
    ans.append('2')
    for _ in range(11):
        ans.append('1')
    for _ in range(5):
        ans.append('1')
        ans.append('2')
    for _ in range(9):
        ans.append('2')
    ans.append('0')
    print(len(ans))
    print("".join(ans))
elif options == "impossible":
    balance = 0
    print(n)
    ans = []
    for _ in range(n):
        x = random.randint(0,2)
        if balance == 0 and x == 1:
            x = 2
        ans.append(str(x))
        if x == 1:
            balance += 1
        if x == 2:
            balance -= 1
    print("".join(ans))
elif options == "big":
    print(n)
    ans = []
    ans.append("1")
    for i in range(1, n):
        if 2*i < n:
            ans.append("2")
        else:
            ans.append("0")
    print("".join(ans))
else:
    voters = []
    balance = []
    balance.append(0)
    fi = []
    ni = []
    ei = []
    ni.append(0)
    for i in range(v):
        x = random.randint(1,2)

        if options == "alternating":
            rest = v // 5
            rest -= rest%2
            if i < rest:
                x = ((i + (i > 1))%2 + 1)
            else:
                x = 2

        if x == 1:
            balance.append(balance[-1] + 1)
        else:
            balance.append(balance[-1] - 1)
        voters.append(x)
        if balance[-1] > 0:
            fi.append(len(balance)-1)
        if balance[-1] == 0:
            ni.append(len(balance)-1)
        if balance[-1] < 0:
            ei.append(len(balance)-1)
    tellers = [0] * (v+1)

    if len(fi) == 0:
        neutral += friend
        friend = 0
    if len(ei) == 0:
        neutral += enemy
        enemy = 0

    for _ in range(0, friend):
        j = random.randrange(0, len(fi))
        tellers[fi[j]] += 1
    for _ in range(0, neutral):
        j = random.randrange(0, len(ni))
        tellers[ni[j]] += 1
    for _ in range(0, enemy):
        j = random.randrange(0, len(ei))
        tellers[ei[j]] += 1
    
    print(n)
    ans = []
    for i in range(0, v):
        for _ in range(tellers[i]):
            ans.append("0")
        ans.append(str(voters[i]))
    for _ in range(tellers[v]):
        ans.append("0")
    print("".join(ans))
