#!/usr/bin/env python3
import sys, argparse, random

# Borrowed from NWERC

parser = argparse.ArgumentParser(description="Generator for Friendly Fire.")
parser.add_argument('-o', metavar='O', type=str, default="random",
                    help='Options for generation')
parser.add_argument('-n', metavar='N', type=int, required=True,
                    help='number of steps')
parser.add_argument('-m', metavar='M', type=int, required=True,
                    help='number of ships')
parser.add_argument('-l1', metavar='L1', type=int, default=1,
                    help='minimum ship length')
parser.add_argument('-l2', metavar='L2', type=int, default=10**6,
                    help='maximum ship length')
parser.add_argument('-s', metavar='S', type=int, default=None,
                    help='seed for generation (optional)')

def overlap(a, b, c):
    for (x, y) in ships_at_y[c]:
        if not (b < x or a > y):
            return True
    if options == "possible":
        if a <= path[c] <= b:
            return True
    return False

args = parser.parse_args()
random.seed(args.s)

options = args.o
n = args.n
m = args.m
l1 = args.l1
l2 = args.l2
l2 = min(l2, 2*n)

path = []  # A random torpedo path, for options == "possible"
path.append(0)
for y in range(1,n):
    path.append(path[-1] + random.randint(-1,1))

ships_at_y = []
for i in range(0,n+1):
    ships_at_y.append([])

if options == "checker":
    ans = []
    for y in range(l1, n):
        for x in range(-y, y+1):
            if (x+y)%2 == 0 and len(ans) < m:
                ans.append((x, x, y))
        if len(ans) == m:
            break
    print(n, len(ans))
    for (a, b, c) in ans:
        print(a,b,c)

elif options == "cave":
    Y = random.sample(list(range(1,2*n-1)), m)
    ans = []
    for i in Y:
        y = 0
        x1 = 0
        x2 = 0
        if i >= n:
            y = i - n + 1
            x1 = path[y] + 1
            x2 = n
        else:
            y = i
            x1 = -n
            x2 = path[y] - 1
        ans.append((x1,x2,y))
    print(n, len(ans))
    for (a, b, c) in ans:
        print(a,b,c)

elif options == "tunnel":
    y = 1
    ans = []
    while y < n and m > 1:
        ans.append((-n, -1, y))
        ans.append((1, n, y))
        m -= 2
        y += 1
    print(n, len(ans))
    for (a, b, c) in ans:
        print(a, b, c)

elif options == "chain":
    ships_at_y[1].append((-1, -1))
    ships_at_y[1].append((1, 1))
    m -= 2
    y = n-1
    start = max(-n, -100)
    while m > 0 and y > 1:
        ships_at_y[y].append((start, start+1))
        start += 1
        y -= 1
        m -= 1
    ans = []
    for y in range(0, n+1):
        for (a, b) in ships_at_y[y]:
            ans.append((a, b, y))
    print(n, len(ans))
    for (a, b, c) in ans:
        print(a,b,c)

elif options == "pyramid":
    base = l1
    blocks = l2
    if base%2 == 0:
        base += 1
    ships = 0
    start = (base + 1)//2
    while start < n and ships < m:
        for i in range(0, start // ((base + 1) // 2)):
            x = -start + i * (base + 1)
            ships_at_y[start].append((x + 1, x + base))
            ships += 1
            if ships == m:
                break
        start += (base + 1)//2

    ans = []
    ind = []
    for y in range(1, n):
        for (a, b) in ships_at_y[y]:
            ans.append((a,b,y))
            ind.append(len(ind))
    m = len(ans)
    blocks = min(blocks, m)
    blocked = random.sample(ind, blocks)
    for i in blocked:
        ans[i] = (ans[i][0] - 1, ans[i][1], ans[i][2])

    random.shuffle(ans)
    print(n, len(ans))

    block_right = False
    if blocks > 0:
        block_right = True

    for (a, b, c) in ans:
        if b == c - 1 and block_right:
            block_right = False
            b += 1
        print(a, b, c)

elif options == "tworows":
    y  = random.randrange(1, n-1)
    X1 = []
    X2 = []
    for i in range(0, m):
        if random.randint(0, 1) == 0:
            x = random.randint(-y, y)
            X1.append(x)
        else:
            x = random.randint(-y-1, y+1)
            X2.append(x)
    X1 = list(set(X1))
    X2 = list(set(X2))
    X1.sort()
    X2.sort()
    for i in range(0, len(X1)):
        nex = n+1
        x = X1[i]
        if i+1 < len(X1):
            nex = X1[i+1]
        b = random.randint(x+l1, x+l2)
        b = min(b, nex - 1)
        ships_at_y[y].append((x, b))
    for i in range(0, len(X2)):
        nex = n+1
        x = X2[i]
        if i+1 < len(X2):
            nex = X2[i+1]
        b = random.randint(x+l1, x+l2)
        b = min(b, nex - 1)
        ships_at_y[y+1].append((x, b))
    ans = []
    for y in range(1, n):
        for (a, b) in ships_at_y[y]:
            ans.append((a,b,y))
    random.shuffle(ans)

    print(n, len(ans))
    for (a, b, c) in ans:
        print(a, b, c)
else:
    lim = 100

    for i in range(0, m):
        a = random.randrange(-n,n+1)
        b = random.randint(a+l1, a+l2)
        b = min(b, n)
        c = random.randrange(1,n)

        tries = 0
        while overlap(a, b, c):
            if tries == lim:
                break
            a = random.randrange(-n,n+1)
            b = random.randint(a+l1, a+l2)
            b = min(b, n)
            c = random.randrange(1,n)
            tries += 1
        if tries < lim:
            ships_at_y[c].append((a, b))
        else:
            break

    ans = []
    for y in range(1, n):
        for (a, b) in ships_at_y[y]:
            ans.append((a,b,y))
    random.shuffle(ans)

    print(n, len(ans))
    for (a, b, c) in ans:
        print(a, b, c)
