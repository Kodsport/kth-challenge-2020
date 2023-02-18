#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

int n,m;
vector<vector<pii> > ships(1000001, vector<pii>());

string ANS = "";

string mzp = "-0+";

int tries = 0;
int lim = 10000000;

bool overlap(int x, int y){
    trav(p, ships[y]){
        if(p.first <= x && x <= p.second)return 1;
        tries++;
    }
    return 0;
}

bool run(int dx = -2){
    int x = 0;
    ANS = "";
    rep(y,1,n+1){
        tries++;
        int d = dx;
        if(dx == -2){
            d = rand()%3-1;
        }
        x += d;
        if(overlap(x, y))return 0;
        ANS += mzp[d+1];
    }
    return 1;
}

int main() {
    cin >> n >> m;
    rep(c1,0,m){
        int a,b,c;
        cin >> a >> b >> c;
        ships[c].push_back({a,b});
    }
    rep(c1,0,n){
        sort(all(ships[c1]));
    }
    if(run(-1)){
        cout << ANS << "\n";
        return 0;
    }
    if(run(0)){
        cout << ANS << "\n";
        return 0;
    }
    if(run(1)){
        cout << ANS << "\n";
        return 0;
    }
    while(tries < lim){
        if(run(-2)){
            cout << ANS << "\n";
            return 0;
        }
    }
    cout << "impossible\n";
    return 0;
}

