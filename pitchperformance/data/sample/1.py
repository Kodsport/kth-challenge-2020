import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fx = [0, 3, 10]
fy = [20, 10]

gx = [0, 2, 4, 10]
ga = [2, -4, 0]
gb = [0, 16, 1]
gc = [10, 10, 6]

def f(x):
    i = 0
    while x >= fx[i+1]: i += 1
    return fy[i]

def g(x):
    i = 0
    while x >= gx[i+1]: i += 1
    return ga[i]*x*x + gb[i]*x + gc[i]

X = []
x0 = 0
for x1 in sorted(set(fx+gx)):
    if x1 > x0:
        for i in range(10*(x1-x0)):
            X.append(x0 + 0.1*i)
        X.append(x1-1e-9)
    x0 = x1

F = [f(x) for x in X]
G = [g(x) for x in X]

plt.plot(X, F, color='b', label=r'$f(x)$')
plt.plot(X, G, color='r', label=r'$g(x)$')
plt.fill_between(X, F, G, facecolor='#bbbbbb')
plt.legend()
plt.savefig('1.pdf', bbox_inches='tight')
