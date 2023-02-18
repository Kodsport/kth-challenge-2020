#!/usr/bin/env pypy
import os
import random
import sys

MAX_D = 40
MAX_B = 500
MAX_F = 100

CASE = 1
DEST = os.path.join(os.path.dirname(__file__), '../data/secret')

def next_file(short_desc=None, long_desc=None):
    global CASE
    basename = os.path.join(DEST, '%03d' % CASE)
    CASE += 1
    if short_desc is not None:
        basename += '-' + short_desc
    if long_desc is not None:
        with open(basename+'.desc', 'w') as desc_out:
            desc_out.write(long_desc)
    return open(basename+'.in', 'w')

def save_case(d, b, f, t0, t1, t2, short_desc=None, long_desc=None):
    out = next_file(short_desc=short_desc, long_desc=long_desc)
    out.write('%d %d %d %d %d %d\n' % (d, b, f, t0, t1, t2))
    out.close()

    
def gen_uniform_case(d_val=None):
    d = random.randint(1, MAX_D) if not d_val else d_val
    b = random.randint(1, MAX_B)
    f = random.randint(1, MAX_F)
    t0 = random.randint(1, MAX_F)
    t1 = random.randint(1, MAX_F)
    t2 = random.randint(1, MAX_F)
    save_case(d, b, f, t0, t1, t2, short_desc='uniformly_random')

def geo(p): # E[x] = (1-p)/p
    x = 0
    while random.random() > p: x += 1
    return x
    
def gen_geometric_case(d_val=None):
    # Each resource independently geometrically distributed with mean 1
    d = random.randint(1, MAX_D) if not d_val else d_val
    b = 100*geo(0.5) + random.randint(0, 99) # bling only matters in multiples of 100
    f = geo(0.5)
    t0 = geo(0.5)
    t1 = geo(0.5)
    t2 = geo(0.5)
    save_case(d, b, f, t0, t1, t2, short_desc='geometric_random')


def main():
    random.seed(2020)

    save_case(10, 0, 1, 0, 0, 0, short_desc='singlefruit')
    save_case(10, 0, 0, 1, 0, 0, short_desc='singletree')
    for i in range(1, 11):
        gen_geometric_case(d_val=i)
    for _ in range(10):
        gen_uniform_case(d_val=i)
    for _ in range(20):
        gen_geometric_case()
    for _ in range(10):
        gen_uniform_case()

    save_case(11, 0, 1, 1, 0, 0, short_desc='kill_greedy_exotic')
    save_case(MAX_D, 0, 2, 2, 0, 0, short_desc='kill_greedy_exotic')
    save_case(MAX_D, 0, 1, 0, 1, 0, short_desc='manystates')
    save_case(MAX_D, 0, 2, 0, 0, 0, short_desc='manystates')
    save_case(MAX_D, 0, 1, 1, 1, 0, short_desc='manystates')
    save_case(MAX_D, 0, 1, 0, 1, 1, short_desc='manystates')
    save_case(MAX_D, 0, 3, 0, 1, 1, short_desc='manystates')
    save_case(MAX_D, 0, 4, 0, 1, 1, short_desc='manystates')
    save_case(MAX_D, 0, 5, 0, 1, 1, short_desc='manystates')
        
    for d in [1, MAX_D]:
        for b in [0, MAX_B]:
            for f in [0, MAX_F]:
                for t0 in [0, MAX_F]:
                    for t1 in [0, MAX_F]:
                        for t2 in [0, MAX_F]:
                            if (b >= 400) + f + t0 + t1 + t2:
                                save_case(d, b, f, t0, t1, t2, short_desc='extremal')
    

if __name__=='__main__':
    main()
