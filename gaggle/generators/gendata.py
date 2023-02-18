#!/usr/bin/env pypy
import os
import random
import sys

MAX_N = 500000

CASE = 11
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

def save_case(T, short_desc=None, long_desc=None):
    n = len(T)
    shuf = range(n)
    random.shuffle(shuf)
    invshuf = range(n)
    for i in range(n): invshuf[shuf[i]] = i
    
    sys.stderr.write('save n=%d short_desc %s\n' % (n, short_desc))
    f = next_file(short_desc=short_desc, long_desc=long_desc)
    f.write('%s\n' % n)
    f.write('%s\n' % ' '.join('%d' % (shuf[T[invshuf[i]]]+1) for i in range(n)))
    f.close()

def rand_fun(V):
    T = {}
    for v in V:
        while True:
            T[v] = random.choice(V)
            if T[v] != v: break
    return T

def cycle(V):
    T = {}
    for i in range(len(V)):
        T[V[i]] = V[i-1]
    return T

def rand_type(V):
    return random.choice([rand_fun, cycle])(V)

def rand_fun_leaf_count(V, leaves):
    NonLeaves = random.sample(V, len(V)-leaves)
    while True:
        random.shuffle(V)
        if not any(V[i] == NonLeaves[i] for i in range(len(NonLeaves))):
            break
    T = {}
    for i in range(len(V)):
        if i < len(NonLeaves): T[V[i]] = NonLeaves[i]
        else: T[V[i]] = random.choice(NonLeaves)
    return T


def rand_case(n):
    save_case(rand_fun(range(n)), short_desc='random_n%d' % n)

def rand_many_small_components(n, max_comp_size, component_generator, short_desc=None, long_desc=None):
    T = {}
    while n > 0:
        sz = random.randint(2, max_comp_size)
        if n - sz == 1 or sz > n: sz = n
        T.update(component_generator(range(n-sz, n)))
        n -= sz
    save_case(T, short_desc=short_desc, long_desc=long_desc)
    
    

def main():
    global CASE

    random.seed(42)
    
    CASE = 1
    save_case(cycle(range(10)), short_desc='small_onecycle')
    save_case([9]*9 + [1], short_desc='small_star')
    rand_many_small_components(10, 2, cycle, short_desc='small_pairs')
    rand_many_small_components(10, 7, cycle, short_desc='small_fewcycles')

    # room for adding a few more small cases here
    
    random.seed(2020)
    CASE = 11

    for _ in range(5):
        n = random.randint(5, 20)
        rand_case(n)

    save_case(cycle(range(MAX_N)), short_desc='max_onecycle')
    rand_many_small_components(MAX_N, 100, cycle, short_desc='max_manycycles')

    save_case([MAX_N-1]*(MAX_N-1) + [1], short_desc='max_star')
    rand_many_small_components(MAX_N, 2*MAX_N/3, cycle, short_desc='max_fewcycles')
    rand_many_small_components(MAX_N, 2, cycle, short_desc='max_pairs')

    for _ in range(5):
        n = random.randint(2, MAX_N)
        max_comp_scale = random.randint(1, n.bit_length())
        max_comp = min(random.randint(2, 1<<max_comp_scale), n)
        gen = random.choice([rand_fun, cycle, rand_type])
        rand_many_small_components(n, max_comp, gen, long_desc='n = %d\nmax component size = %d\ncomponent generator = %s\n' % (n, max_comp, gen.__name__))

              
if __name__=='__main__':
    main()
