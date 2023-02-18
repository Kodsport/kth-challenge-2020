#include <bits/stdc++.h>
#include "validate.h"

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef long double ld;

int n,m;

vector<vector<pii> > ships_at_y;

bool impossible(string s){
    string t = "";
    trav(ch, s){
        t += tolower(ch);
    }
    return t == "impossible";
}

int diff(char ch){
    if(ch == '-')return -1;
    if(ch == '+')return 1;
    if(ch == '0')return 0;
    return -1234;
}

bool valid_answer(string s){
    if(s.length() != n)return 0;
    int x = 0;
    rep(y,0,n){
        trav(p, ships_at_y[y]){
            if(p.first <= x && p.second >= x)return 0;
        }
        int d = diff(s[y]);
        if(d == -1234)return 0;
        x += d;
    }
    return 1;
}

void check_case(){
    judge_in >> n >> m;
    rep(c1,0,n+1){
        vector<pii> temp;
        ships_at_y.push_back(temp);
    }
    rep(c1,0,m){
        int a,b,c;
        judge_in >> a >> b >> c;
        ships_at_y[c].push_back({a,b});
    }

    string judge_answer, author_answer;

    if(!(author_out >> author_answer)){
        wrong_answer("Could not read contestants output\n");
    }
    if(!(judge_ans >> judge_answer)){
        judge_error("Could not read judge output\n");
    }
    if(!valid_answer(author_answer)){
        if(!impossible(author_answer)){
            wrong_answer("Contestants output was not valid\n");
        }
        else{
            if(impossible(judge_answer)){
                return;
            }
            else{
                wrong_answer("Contestant says impossible, but it is possible\n");
            }
        }
    }

    if(impossible(judge_answer)){
        judge_error("Judge says impossible, but contestant found a solution\n");
    }
}

int main(int argc, char **argv) {
  init_io(argc, argv);
  check_case();

  /* Check for trailing output. */
  string trash;
  if (author_out >> trash) {
      wrong_answer("Trailing output\n");
  }

  accept();
  return 0;
}