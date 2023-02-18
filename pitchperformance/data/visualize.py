import bisect
import sys
import matplotlib.pyplot as plt

N = 1000

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

outname = sys.argv[1] if len(sys.argv) >= 2 else None

n = int(raw_input())
fx = []
fy = []
for _ in range(n):
    (x, y) = map(int, raw_input().split())
    fx.append(x)
    fy.append(y)

m = int(raw_input())
gx = []
ga = []
gb = []
gc = []
for _ in range(m):
    (x, a, b, c) = map(int, raw_input().split())
    gx.append(x)
    ga.append(a)
    gb.append(b)
    gc.append(c)

def f(x):
    i = bisect.bisect(fx, x)
    return fy[i]

def g(x):
    i = bisect.bisect(gx, x)
    return ga[i]*x*x + gb[i]*x + gc[i]

bx = sorted(set(fx+gx))
s = len(bx)

N = max(N, 2*s+1)

dx = 1.0*fx[-1]/(N-2*s)

X = sorted(set([i*dx for i in range(N-2*s)] +
               [x-1e-9 for x in bx] +
               [x for x in bx[:-1]]))

F = [f(x) for x in X]
G = [g(x) for x in X]

plt.plot(X, F, color='b', label=r'$f(x)$')
plt.plot(X, G, color='r', label=r'$g(x)$')
plt.fill_between(X, F, G, facecolor='#bbbbbb')
plt.legend()
if outname:
    plt.savefig(outname, bbox_inches='tight')
else:
    plt.show()
