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

const int MAXN = 500000;

int n,m;

vi X,Y,L;
vector<vi> ships_at_y(MAXN+1, vi());

int left_end[2*MAXN+2] = {0};
vi T, I, from;

vi current;

void rollback(int t){
    while(sz(T) > 0 && T.back() == t){
        left_end[I.back()] = from.back();
        T.pop_back();
        I.pop_back();
        from.pop_back();
    }
}

void change(int i, int t, int dx){
    T.push_back(t);
    I.push_back(i);
    from.push_back(left_end[i]);
    left_end[i] += dx;
}

bool comp(int i, int j){
    return X[i] < X[j];
}

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
    int intervals = 0;
    for(int y = n-1; y >= 0; y--){
        if(sz(ships_at_y[y]) > 0){
            sort(all(ships_at_y[y]),comp);
        }
        vi merged;
        int p1 = 0;
        int p2 = 0;
        int prev = -1;

        while(p1 < sz(ships_at_y[y]) || p2 < sz(current)){
            intervals++;
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
                    change(X[j], y, -1);
                    j = -1;
                }
                curr = 1;
                p2++;
            }
            if(j != -1){
                if(prev != -1 && X[prev] + L[prev] >= X[j]){
                    L[prev] = max(L[prev], X[j] - X[prev] + L[j]);
                    if(curr)change(X[j], y, -1);
                }
                else{
                    merged.push_back(j);
                    prev = j;
                    if(!curr)change(X[j], y, 1);
                }
            }
        }
        current = merged;
    }

    int x = 0;
    bool fail = 0;
    trav(j, current){
        if(X[j] <= x && X[j] + L[j] - 1 >= x)fail = 1;
    }
    if(fail){
        cout << "impossible\n";
    }
    else{
      //  cerr << intervals << "\n";  //
      //  return 0;  //
        rep(y,0,n){
            rollback(y);
            if(!left_end[x+2] && !left_end[x+1]){
                x += 2;
                cout << '+';
                continue;
            }
            if(!left_end[x+1]){
                x++;
                cout << '0';
                continue;
            }
            if(!left_end[x]){
                cout << '-';
                continue;
            }
        }
        cout << "\n";
    }

    return 0;
}
