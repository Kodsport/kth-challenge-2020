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

// This should get TLE or MLE

const int MAXN = 500000;

int n,m;

vi X,Y,L;
vector<vi> ships_at_y(MAXN+1, vi());

vi current;

bool comp(int i, int j){
    return X[i] < X[j];
}

vector<vector<pii> > danger(MAXN+1, vector<pii>());

int main() {
    cin >> n >> m;
    rep(c1,0,m){
        int a,b,c;
        cin >> a >> b >> c;
        X.push_back(max(0,a+c));
        Y.push_back(c);
        L.push_back(b+c - X.back() + 1);
        ships_at_y[c].push_back(c1);
    }
    for(int y = n-1; y >= 0; y--){
        if(sz(ships_at_y[y]) > 0){
            sort(all(ships_at_y[y]),comp);
        }
        vi merged;
        int p1 = 0;
        int p2 = 0;
        int prev = -1;

        while(p1 < sz(ships_at_y[y]) || p2 < sz(current)){
            int j;
            bool curr = 0;
            if(p2 == sz(current) || (p1 != sz(ships_at_y[y]) && X[ships_at_y[y][p1]] < X[current[p2]])){
                j = ships_at_y[y][p1];
                p1++;
            }
            else{
                j = current[p2];
                L[j]-=2;
                if(L[j] <= 0){
                    j = -1;
                }
                curr = 1;
                p2++;
            }
            if(j != -1){
                if(prev != -1 && X[prev] + L[prev] >= X[j]){
                    L[prev] = max(L[prev], X[j] - X[prev] + L[j]);
                }
                else{
                    merged.push_back(j);
                    prev = j;
                }
            }
        }
        current = merged;
        trav(j, current){
            danger[y].push_back({X[j], X[j] + L[j] - 1});
        }
    }

    int x = 0;
    bool fail = 0;
    trav(p, danger[0]){
        if(p.first <= x && p.second >= x)fail = 1;
    }
    if(fail){
        cout << "impossible\n";
    }
    else{
        rep(y,1,n+1){
            bool bad[3] = {0};
            trav(p, danger[y]){
                rep(dx,0,3){
                    if(p.first <= x+dx && x+dx <= p.second)bad[dx] = 1;
                }
            }
            if(!bad[2]){
                x += 2;
                cout << '+';
                continue;
            }
            if(!bad[1]){
                x++;
                cout << '0';
                continue;
            }
            if(!bad[0]){
                cout << '-';
                continue;
            }
        }
        cout << "\n";
    }

    return 0;
}

