import re
import sys

MAX_ASSUMPTIONS = 5
MAX_N = 400000

fact_re = re.compile('^[A-Z]{1,5}$')

line = sys.stdin.readline()
assert re.match('^[1-9][0-9]*\n$', line)
n = int(line)
assert 1 <= n <= MAX_N

for i in range(n):
    line = sys.stdin.readline()
    assert line[-1] == '\n'
    toks = line[:-1].split(' ')
    assert 2 <= len(toks) <= 2+MAX_ASSUMPTIONS
    for i in range(len(toks)-2):
        assert fact_re.match(toks[i])
    assert toks[-2] == '->'
    assert fact_re.match(toks[-1])

assert sys.stdin.readline() == ''

sys.exit(42)
