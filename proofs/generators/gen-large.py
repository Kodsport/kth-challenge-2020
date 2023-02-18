#!/usr/bin/env pypy
import os
import random
import sys

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
    return (open(basename+'.in', 'w'), open(basename+'.ans', 'w'))

def gen_large_pair(n, desc):
    claims = [""]
    for pos in range(4):
        new_claims = []
        for claim in claims:
            for char in range(26):
                new_claims.append(claim + chr(ord('A') + char))
        claims = new_claims
    random.shuffle(claims)

    lines = [[claims[0]]]
    prove_pos = 0

    # Pick a single bad claim. A little dangerous
    bad_claim = random.randint(1, 4*(n//10))
    bad_line = -1
    for pos in range(1, n):
        # Pick 0 to 5 assumptions
        new_line = [claims[random.randint(0, prove_pos)]
                for _ in range(random.randint(1, 6))]

        # Make sure to include the bad claim somewhere
        if prove_pos == bad_claim:
            if len(new_line) == 1:
                new_line = [claims[bad_claim]] + new_line
            else:
                new_line[0] = claims[bad_claim]

        # Prove something new sometimes
        if random.randint(0, 1):
            prove_pos += 1
            new_line[-1] = claims[prove_pos]
            if prove_pos == bad_claim:
                bad_line = pos
        lines.append(new_line)

    save_case(lines, "correct", short_desc = desc + '-correct')

    # Oops, we never proved the bad claim!
    lines[bad_line][-1] = claims[bad_claim - 1]
    save_case(lines, str(bad_line + 2), short_desc = desc + '-wrong')
    print("made {}".format(n))

def save_case(lines, res, short_desc=None, long_desc=None):
    out, ans = next_file(short_desc=short_desc, long_desc=long_desc)
    out.write(str(len(lines)) + "\n")
    for line in lines:
        out.write(" ".join(line[:-1] + ["->"] + line[-1:]) + "\n")
    out.close()
    ans.write(res + "\n")
    ans.close()
    
def main():
    random.seed(2020)
    
    for _ in range(5):
        gen_large_pair(int(4e5), "long")
    for _ in range(20):
        gen_large_pair(int(4e4), "med")

if __name__=='__main__':
    main()
