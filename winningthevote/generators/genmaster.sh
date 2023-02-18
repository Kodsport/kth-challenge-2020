#!/bin/bash -e

# Set this if you want to generate answers.
g++ -O2 ../submissions/accepted/nils.cpp -o /tmp/a.out
#cp ../../submissions/accepted/solution.py /tmp/sol.py
SOLVER=/tmp/a.out
MAXN=5000

rm -f ../data/secret/*_generated.{in,ans}

generate() {
    ((COUNT++))
    printf -v padCount "%02d" $COUNT
    ./gen.py -s $COUNT -n $1 -friend $2 -neutral $3 -enemy $4 -o $5 > ../data/secret/${padCount}_n$1_$5_generated.in
}

COUNT=15
generate 10 1 2 2 random
generate 40 3 3 3 random
generate 100 1 20 20 random
generate 700 1 20 200 random
generate $MAXN 1 $(($MAXN / 3)) $(($MAXN / 3)) random
generate $MAXN 1 $(($MAXN / 6)) $(($MAXN / 4)) random
generate $MAXN 1 1 1 random
generate $MAXN 1 $(($MAXN / 3)) $(($MAXN / 3)) random
generate $MAXN 1 $(($MAXN / 3)) $(($MAXN / 3)) random
generate $MAXN 1 $(($MAXN / 3)) $(($MAXN / 3)) random
generate $MAXN 0 10 $(($MAXN / 2)) random
generate $MAXN 0 10 $(($MAXN / 2)) random
generate $MAXN 0 10 $(($MAXN - 500)) random
generate $MAXN 0 10 $(($MAXN - 50)) random
generate $MAXN 0 10 100 random
generate $MAXN $(($MAXN / 3)) 0 $(($MAXN / 3)) random
generate $MAXN $(($MAXN / 2)) 0 0 random
generate $MAXN 0 0 0 impossible
generate $MAXN 0 0 0 impossible
generate $MAXN 0 0 0 big
generate 1 0 1 0 random
generate 1 0 0 0 random
generate $MAXN 0 0 0 random
generate $MAXN 0 $(($MAXN / 3)) $(($MAXN / 3)) alternating
generate $MAXN 0 $(($MAXN / 6)) $(($MAXN / 6)) alternating
generate $MAXN 0 2 $(($MAXN / 2)) alternating
generate $MAXN 0 2 $(($MAXN - 10)) alternating
generate $MAXN 0 2 $(($MAXN - 40)) alternating
generate $MAXN 0 2 $(($MAXN - 10)) random
generate 0 1 0 3 tricky
generate 0 0 $(($MAXN / 2 - 101)) $(($MAXN / 2 - 99)) tricky
generate 0 $(($MAXN / 2 - 101)) 0 $(($MAXN / 2 - 99)) tricky

# generate solutions for all files
if [[ ! -z $SOLVER ]]
then
    for f in ../data/secret/*_generated.in
    do
        echo "solving $f"
        $SOLVER < $f > ${f%???}.ans
    done
fi

