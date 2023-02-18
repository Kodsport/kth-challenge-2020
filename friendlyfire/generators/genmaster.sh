#!/bin/bash -e

# Set the problem name to generate correct file names
PROBLEMNAME="friendlyfire"

# Set this if you want to generate answers.
g++ -O2 ../submissions/accepted/nils_nsqrtm.cpp -o /tmp/a.out
#cp ../../submissions/accepted/solution.py /tmp/sol.py
SOLVER=/tmp/a.out
MAXN=500000
MAXM=200000

rm -f ../data/secret/*_generated.{in,ans}

generate() {
    ((COUNT++))
    printf -v padCount "%02d" $COUNT
    ./gen_rand.py -s $COUNT -n $1 -m $2 -l1 $3 -l2 $4 -o $5 > ../data/secret/${padCount}_n$1_m$2_$5_generated.in
}

COUNT=10
generate 2 0 1 50 random
generate 10 4 1 4 random
generate 10 4 1 4 random
generate 100 40 1 40 random
generate 100 40 1 40 random
generate 100 40 1 40 random
generate 2000 4000 1 40 random
generate 2000 2000 30 40 random
generate 2000 4000 1 40 random
generate 2000 6000 1 40 random
generate 2000 28000 1 40 random
generate 2000 40000 1 40 random
generate 2000 20000 1 40 random
generate 2000 40000 30 40 possible
generate 2000 20000 30 40 possible
generate 2000 20000 30 40 possible
generate 2000 10000 30 400 possible
generate 2000 100000 30 400 possible
generate $MAXN $MAXM 1 $MAXN random
generate $MAXN $MAXM 100 10000 random
generate $MAXN $MAXM 50 100 random
generate $MAXN $MAXM 50 100 possible
generate $MAXN $MAXM 500 1000 possible
generate 500 $MAXM 10 20 possible
generate 7 6 3 0 pyramid
generate $MAXN $MAXM 1877 0 pyramid
generate $MAXN $MAXM 1577 0 pyramid
generate $MAXN $MAXM 1000 0 pyramid
generate $MAXN $MAXM 800 0 pyramid
generate $MAXN $MAXM 500 0 pyramid
generate 7 6 3 6 pyramid
generate $MAXN $MAXM 1577 7 pyramid
generate $MAXN $MAXM 1577 700 pyramid
generate $MAXN $MAXM 1577 7000 pyramid
generate $MAXN $MAXM 1577 20000 pyramid
generate $MAXN $MAXM 1577 40000 pyramid
generate $MAXN $MAXM 1577 70000 pyramid
generate 10 20 2 5 tworows
generate $MAXN $MAXM 1 100 tworows
generate $MAXN $MAXM 100 10000 tworows
generate $MAXN $MAXM 1 3 tworows
generate $MAXN $MAXM 1 1 random
generate 700 $MAXM 1 1 possible
generate $MAXN $MAXM 50000 100000 possible
generate $MAXN $MAXM $(($MAXN / 2)) $MAXN random
generate $MAXN $MAXM 0 0 chain
generate $MAXN $MAXM 0 0 tunnel
generate $MAXN $MAXM 0 0 cave
generate $MAXM $MAXM 0 0 cave
generate $MAXN $MAXM 40000 0 checker
generate $MAXN $MAXM 1 0 checker

# generate solutions for all files
if [[ ! -z $SOLVER ]]
then
    for f in ../data/secret/*_generated.in
    do
        echo "solving $f"
        $SOLVER < $f > ${f%???}.ans
    done
fi

