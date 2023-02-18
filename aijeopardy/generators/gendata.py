#!/usr/bin/env pypy
import os
import random
import sys

MAX_X = 10**100

CASE = 1
DEST = os.path.join(os.path.dirname(__file__), '../data/secret')

def next_file(short_desc=None, long_desc=None):
    global CASE
    basename = os.path.join(DEST, '%02d' % CASE)
    CASE += 1
    if short_desc is not None:
        basename += '-' + short_desc
    if long_desc is not None:
        with open(basename+'.desc', 'w') as desc_out:
            desc_out.write(long_desc)
    return open(basename+'.in', 'w')

seen = set([10, 2020]) # samples

def save_case(n, short_desc=None, long_desc=None):
    if n in seen: return
    seen.add(n)
    sys.stderr.write('save log(n)=%d short_desc %s\n' % (n.bit_length(), short_desc))
    f = next_file(short_desc=short_desc, long_desc=long_desc)
    f.write('%s\n' % n)
    f.close()

def binom(n, k):
    res = 1
    for i in range(k): res = res*(n-i)/(i+1)
    return res

def max_n(k):
    lo = 2*k
    hi = 2*lo
    while binom(hi, k) <= MAX_X:
        lo = hi
        hi = 2*hi
    while hi-lo > 1:
        n = (lo+hi)/2
        if binom(n, k) <= MAX_X:
            lo = n
        else:
            hi = n
    return lo

def max_case(k):
    return binom(max_n(k), k)

    
def rand_case(k):
    n_lim = max_n(k)
    n = random.randint(2*k, n_lim)
    return binom(n, k)


def main():
    random.seed(2020)

    for i in range(2, 21):
        save_case(i, short_desc='x%d' % i)

    save_case(random.randint(21, 1000))
    save_case(binom(32, 16))
    save_case(MAX_X)

    max_k = 2
    while binom(2*(max_k+1), max_k+1) <= MAX_X:
        max_k += 1

    for _ in range(20):
        k = random.randint(1, max_k)
        t = random.randint(1, 3)
        if t == 1:
            save_case(rand_case(k), short_desc='rand_k%d' % k)
        elif t == 2:
            save_case(max_case(k), short_desc='max_k%d' % k)
        elif t == 3:
            save_case(max_case(k)+random.choice([-1,1]), short_desc='max_almost_k%d' % k)

    for _ in range(5):
        scale = random.randint(1, 100) # Assumes MAX_X = 10**100
        save_case(random.randint(1, 10**scale))
        
    save_case(max_case(max_k), short_desc='max_k%d' % max_k)
    save_case(max_case(max_k)+random.choice([-1,1]), short_desc='max_almost_k%d' % max_k)

if __name__=='__main__':
    main()
