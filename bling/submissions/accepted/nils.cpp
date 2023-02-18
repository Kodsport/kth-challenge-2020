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

ll end_fruit(ll d){
    if(d <= 0)return 0;
    ll t = 1;
    rep(c1,0,(d-1)/3){
        t *= 4;
    }
    return t*3;
}

const ll base = 12445;
map<ll,ll> DP;

ll dp(ll d, ll bling, ll fruit, vl trees, vl exotic){
        if(d == 0)return 100 * bling;
        ll extra = 0;

        if(bling > 12){
            extra += 100 *(bling-12);
            bling = 12;
        }
        
        if(fruit > 12){
            extra += 100 * max(fruit-12, end_fruit(d-3) * (fruit-12));
            fruit = 12;
        }

        rep(i,0,3){
            if(trees[i] > 4){
                extra += 100 * (trees[i] - 4) * end_fruit(d-i);
                trees[i] = 4;
            }
            if(exotic[i] > 1){
                extra += 500 * (exotic[i] - 1) * end_fruit(d-i);
                exotic[i] = 1;
            }
        }

        vl stuff;
        stuff.push_back(d);
        stuff.push_back(bling);
        stuff.push_back(fruit);
        trav(t, trees){
            stuff.push_back(t);
        }
        trav(t, exotic){
            stuff.push_back(t);
        }
        ll h = 0;
        trav(t, stuff){
            h *= base;
            h += t;
        }
        if(DP.find(h) != DP.end())return (extra + DP[h]);

        // Transitions

        ll ans = 0;

        ll tot_fruit = fruit + 3*trees[0];
        ll exo = 3*exotic[0];

        rep(sell1, 0, tot_fruit+1){
            rep(sell2, 0, exo+1){
                ll tot_bling = 100 * bling + 100 * sell1 + 500 * sell2;
                vl trees2 = {trees[1], trees[2], trees[0] + tot_fruit - sell1};
                vl exotic2 = {exotic[1], exotic[2], exotic[0] + exo - sell2};

                // Don't buy exotic
                ll temp1 = dp(d-1, tot_bling/100, 0, trees2, exotic2);
                ans = max(temp1, ans);

                // Buy exotic and sell
                if(tot_bling >= 400){
                    ll temp2 = dp(d-1, tot_bling/100 + 1, 0, trees2, exotic2);
                    ans = max(temp2, ans);
                }

                // Buy exotic and plant
                if(tot_bling >= 400){
                    exotic2[2]++;
                    ll temp3 = dp(d-1, tot_bling/100 - 4, 0, trees2, exotic2);
                    ans = max(temp3, ans);
                }
            }
        }


        DP[h] = ans;
        return extra + ans;
}

int main() {
    int d,b,f,t0,t1,t2;
    cin >> d >> b >> f >> t0 >> t1 >> t2;
    ll ans = b%100;
    b /= 100;

    ans += dp(d, b, f, {t0, t1, t2}, {0, 0, 0});
    cout << ans << "\n";

    return 0;
}

