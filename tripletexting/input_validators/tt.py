#!/usr/bin/env python3
import re
import sys

s = sys.stdin.readline()
assert re.match("^[a-z]+\n$", s)
s = s[:-1]

assert 3 <= len(s) <= 99
assert len(s) % 3 == 0
n = len(s)//3
errs = 0
for i in range(n):
    c = len(set([s[i], s[i+n], s[i+2*n]]))
    assert c <= 2
    if c != 1: errs += 1

assert errs <= 1

assert sys.stdin.readline() == ''
sys.exit(42)
