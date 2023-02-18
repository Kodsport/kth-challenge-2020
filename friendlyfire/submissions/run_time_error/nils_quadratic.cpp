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

char sgn(int x){
    if(x < 0)return '-';
    if(x > 0)return '+';
    return '0';
}

bool DP[4003][2001] = {0};
int NEXT[4003][2001] = {0};

int main() {
    int n,m;
    cin >> n >> m;
    vector<vector<pii>> ships_at_y(n);
    rep(c1,0,m){
        int a,b,c;
        cin >> a >> b >> c;
        ships_at_y[c].push_back({a,b});
    }

    for(int y = n; y >= 0; y--){
        for(int x = -n; x <= n; x++){
            int x2 = x+2001;
            if(y == n){
                DP[x2][y] = 1;
            }
            else{
                for(int dx = -1; dx <= 1; dx++){
                    int x3 = x2 + dx;
                    if(DP[x3][y+1]){
                        DP[x2][y] = 1;
                        NEXT[x2][y] = dx;
                        break;
                    }
                }
            }
        }
        if(y != n){
            trav(p, ships_at_y[y]){
                rep(x, p.first, p.second+1){
                    DP[x+2001][y] = 0;
                }
            }
        }
    }

    if(!DP[2001][0]){
        cout << "impossible\n";
    }
    else{
        int x2 = 2001;
        rep(c1,0,n){
            cout << sgn(NEXT[x2][c1]);
            x2 += NEXT[x2][c1];
        }cout << "\n";
    }

    return 0;
}

