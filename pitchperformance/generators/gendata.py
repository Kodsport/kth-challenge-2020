#!/usr/bin/env pypy
import os
import random
import sys
from math import floor, ceil

MAX_N = 500
MAX_M = 500

MAX_X = 10**4
MAX_Y = 10**4
MAX_COEFF = 10**7

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

def save_case(F, G, short_desc=None, long_desc=None):
    n = len(F)
    m = len(G)
    sys.stderr.write('save n=%d m=%d short_desc %s\n' % (n, m, short_desc))
    f = next_file(short_desc=short_desc, long_desc=long_desc)
    f.write('%d\n' % n)
    for (x, y) in F:
        f.write('%d %d\n' % (x, y))
    f.write('%d\n' % m)
    for (x, a, b, c) in G:
        f.write('%d %d %d %d\n' % (x, a, b, c))
    f.close()

def rand_xs(n, x_end):
    X = sorted(random.randint(1, x_end-n+1) for _ in range(n-1))
    for i in range(n-1): X[i] += i
    X.append(x_end)
    return X

def rand_f(n, x_end):
    X = rand_xs(n, x_end)
    Y = [random.randint(0, MAX_Y) for _ in range(n)]
    return zip(X, Y)

def rand_const(x0, x1):
    return (0, 0, random.randint(0, MAX_Y))

def rand_lin(x0, x1):
    c_min = -MAX_COEFF
    c_max = MAX_COEFF
    if x0 == 0:
        c_min = 0
        c_max = MAX_Y
    while True:
        c = random.randint(-MAX_COEFF, MAX_COEFF)
        if 0 <= c <= MAX_Y:
            b_min = ceil(-c/x1)
            b_max = floor((MAX_Y-c)/x1)
        elif c < 0:
            b_min = ceil(-c/x0)
            b_max = ceil((MAX_Y-c)/x1)
        elif c > MAX_Y:
            b_min = ceil(-c/x1)
            b_max = ceil((MAX_Y-c)/x0)
        b_min = max(b_min, -MAX_COEFF)
        b_max = min(b_max, MAX_COEFF)
        if b_min <= b_max:
            b = random.randint(b_min, b_max)
            return (0, b, c)
        c_min = 9*c_min/10
        c_max = 9*c_max/10

def rand_quad(x0, x1):
    extra = max((x1-x0)/10, 1)
    max_a = int(floor(MAX_Y/(x1-x0)**2))
    max_a = min(max_a, MAX_COEFF/(x1*x1))
    while True:
        a = random.randint(-max_a, max_a)
        if a:
            b_min = -(x1+extra)*(2*a)
            b_max = -(x0-extra)*(2*a)
            if b_min > b_max: (b_min, b_max) = (b_max, b_min)
        
            b = random.randint(b_min, b_max)

        else:
            b = random.randint(-MAX_Y/(x1-x0), MAX_Y/(x1-x0))    

        vals = [a*x0*x0 + b*x0, a*x1*x1 + b*x1]
        if a and x0 <= -b/(2.0*a) <= x1:
            vals.append(-b*b/(4.0*a))

        cmin = max(ceil(-min(vals)), -MAX_COEFF)
        cmax = min(floor(MAX_Y-max(vals)), MAX_COEFF)
        
        if cmin > cmax:
            max_a = 9*max_a/10
            continue
        
        c = random.randint(cmin, cmax)

        return (a, b, c)
    

def rand_piece_rand_deg(x0, x1):
    deg = random.randint(0, 2)
    if deg == 2: return rand_quad(x0, x1)
    elif deg == 1: return rand_lin(x0, x1)
    else: return rand_const(x0, x1)

def rand_g(n, x_end):
    X = [0] + rand_xs(n, x_end)
    Q = [rand_quad(X[i], X[i+1]) for i in range(n)]
    return [(x, a, b, c) for (x, (a, b, c)) in zip(X[1:], Q)]

def rand_g_rand_degs(n, x_end):
    X = [0] + rand_xs(n, x_end)
    Q = [rand_piece_rand_deg(X[i], X[i+1]) for _ in range(n)]
    return [(x, a, b, c) for (x, (a, b, c)) in zip(X[1:], Q)]
    

    
def gen_rand_case(n, m, g_gen=rand_g):
    x_end = random.randint(max(n, m), MAX_X)
    save_case(rand_f(n, x_end), rand_g(m, x_end))

def gen_equal(n):
    x_end = MAX_X
    F = rand_f(n, x_end)
    G = [(x, 0, 0, y) for (x, y) in F]
    save_case(F, G, short_desc='equal')
    
def gen_max_crossings(n):
    xf = range(4, 4*(n+1), 4)
    yf = [100, 104]*(n/2+1)
    F = zip(xf, yf)

    G = []

    for i in range(n):
        prevx = G[i-1][0] if i else 0
        if i % 2 == 0:
            x = xf[i] - (i < n-1)
            midx = (x+prevx)/2
            max_a = min(5, ceil((MAX_COEFF-101)/(midx*midx)))
            a = random.randint(1, max_a)
            b = -2*a*midx
            c = a*midx*midx
            if random.randint(0, 1):
                c += 99
            else:
                c = 101-c
                a = -a
                b = -b
        else:
            x = xf[i] + (i < n-1)
            assert x-prevx == 6 or i == n-1, i
            midx = (x+prevx+1)/2
            a = -1
            b = 2*midx
            c = 106 - midx*midx
        assert abs(c) <= MAX_COEFF, (i, a, b, c)
        G.append((x, a, b, c))
    save_case(F, G, short_desc='max_crossings')
    

def main():
    global MAX_X, MAX_Y
    
    random.seed(2020)

    gen_max_crossings(2)
    gen_max_crossings(3)
    gen_max_crossings(4)
    gen_equal(2)

    save_case([(MAX_X, MAX_Y)], [(MAX_X, 0, 0, 0)], short_desc='maxanswer')
    save_case([(MAX_X, 0)], [(MAX_X, 0, 0, MAX_Y)], short_desc='maxanswer')

    MAX_X = 100
    
    for _ in range(3):
        n = random.randint(1, 5)
        m = random.randint(1, 5)
        gen_rand_case(n, m)

    for _ in range(3):
        n = random.randint(1, 5)
        m = random.randint(1, 5)
        gen_rand_case(n, m, g_gen=rand_g_rand_degs)

    gen_max_crossings(20)
    
    MAX_X = 1000

    for _ in range(4):
        n = random.randint(1, 50)
        m = random.randint(1, 50)
        gen_rand_case(n, m)

    MAX_X = 10**4
    
    for _ in range(4):
        n = random.randint(1, MAX_N)
        m = random.randint(1, MAX_M)
        gen_rand_case(n, m)
    
    for _ in range(4):
        n = random.randint(1, MAX_N)
        m = random.randint(1, MAX_M)
        gen_rand_case(n, m, g_gen=rand_g_rand_degs)

    gen_rand_case(1, MAX_M)
    gen_rand_case(1, MAX_M, g_gen=rand_g_rand_degs)
    gen_rand_case(MAX_N, 1)
    gen_rand_case(MAX_N, 1, g_gen=rand_g_rand_degs)
    gen_rand_case(MAX_N, MAX_M)
    gen_rand_case(MAX_N, MAX_M, g_gen=rand_g_rand_degs)
    gen_max_crossings(MAX_N)
    gen_equal(MAX_N)



if __name__=='__main__':
    main()
