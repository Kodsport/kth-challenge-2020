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
typedef vector<ll> vl;

ll D, F;

ll solve(int d, vi start, vi sell_ex, vl trees, vl trees2, vl exotic, ll bling){
    if(d == 0)return bling;
    trees[d%3] += trees2[d%3];
    trees2[d%3] = 0;

    ll fruit = trees[d%3]*3;
    ll exo = exotic[d%3]*3;

    if(d == D)fruit += F;

    if(d <= 3){
        // End game: sell everything. Don't forget to buy/sell exotic if possible
        bling += 100*fruit + 500*exo;
        if(bling >= 400)bling += 100;
        return solve(d-1, start, sell_ex, trees, trees2, exotic, bling);
    }

    if(d <= start[d%3]){
        if(bling >= 400){
            bling -= 400;
            exo++;
        }
        else{
            if(exo > 0 && sell_ex[d%3]){
                bling += 100;
            }
            else{

                // First: sell fruit to afford.
                while(bling < 400 && fruit > 0){
                    bling += 100;
                    fruit--;
                }


                // Second: sell trees from prev day to afford.
                while(bling < 400 && trees2[(d+1)%3] > 0){
                    bling += 100;
                    trees2[(d+1)%3]--;
                }

                // Third: sell trees from two days prior to afford.
                while(bling < 400 && trees2[(d+2)%3] > 0){
                    bling += 100;
                    trees2[(d+2)%3]--;
                }

                if(bling >= 400){
                    bling -= 400;
                    exo++;
                }
            }
        }
    }

    // Just plant everything:
    trees2[d%3] = fruit;
    exotic[d%3] += exo;
    return solve(d-1, start, sell_ex, trees, trees2, exotic, bling);
}

int main() {

    int d, b, f, t0, t1, t2;

    cin >> d >> b >> f >> t0 >> t1 >> t2;
    D = d;
    F = f;


    ll T[3] = {0};
    T[d%3] = t0;
    T[(d+2)%3] = t1;
    T[(d+1)%3] = t2;

    ll ans = 0;

    rep(s0, 0, d+1){
        rep(s1, 0, d+1){
            rep(s2, 0, d+1){
                rep(se0, 0, 2){
                    rep(se1,0 , 2){
                        rep(se2, 0, 2){
                            ll temp = solve(d, {s0, s1, s2}, {se0, se1, se2}, {T[0], T[1], T[2]}, {0,0,0}, {0,0,0}, b);
                            ans = max(temp, ans);
                        }
                    }
                }
            }
        }
    }

    cout << ans << "\n";

    return 0;
}

