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

const int MAXN = 200000;

int n;
string s;

vi P, Z, B;

vi ind, I, W;

set<pii> S;

bool comp(int i, int j){
    return W[i] < W[j];
}

ll sum = 0;
int min_rm = 0;
void rm(){
    auto it = S.end();
    it--;
    int w = (*it).first;
    sum -= w;
    min_rm = min(min_rm, w);
    if(min_rm == 0)min_rm = w;
    S.erase(*it);
}

int main() {
    cin >> n;
    cin >> s;
    int need = 1;
    int balance = 0;
    bool possible = 0;
    bool teller = 0;
    trav(ch, s){
        if(ch == '1')balance++;
        if(ch == '2')balance--;
        if(ch == '0'){
            teller = 1;
            if(balance > 0)need--;
            if(balance < 0)need++;
        }
        B.push_back(balance);
        P.push_back(n);
        Z.push_back(n);
        if(balance > 0)possible = 1;
    }
    if(!possible || !teller){
        cout << "impossible\n";
        return 0;
    }
    if(need <= 0){
        cout << "0\n";
        return 0;
    }
    for(int rev = 0; rev < 2; rev++){
        int voters = 0;
        int last_zero = -rev*n;
        int last_positive = -n;
        for(int i2 = 0; i2 < n; i2++){
            int i = i2;
            if(rev == 1)i = n-i2-1;
            if(s[i] != '0'){
                if(rev == 0)voters++;
                if(B[i] > 0)last_positive = voters;
                if(B[i] == 0)last_zero = voters;
                if(rev == 1)voters++;
            }
            else{
                P[i] = min(P[i], abs(voters - last_positive));
                Z[i] = min(Z[i], abs(voters - last_zero));
            }
        }
    }
    vi penalty;
    rep(i,0,n){
        if(s[i] == '0'){
            if(B[i] < 0){
                if(Z[i] < P[i] - Z[i]){
                    S.insert({Z[i], i});
                    S.insert({P[i] - Z[i], i});
                    sum += P[i];
                }
                else{
                    ind.push_back(sz(ind));
                    I.push_back(i);
                    W.push_back(P[i]);
                }
            }
            if(B[i] == 0){
                S.insert({P[i],i});
                sum += P[i];
            }
        }
    }

    while(sz(S) > need){
        rm();
    }
    ll ans = 1e16;
    if(sz(S) == need)ans = sum;

    sort(all(ind), comp);
    int max_second = -n;
    for(int j = 0; j < sz(ind); j++){
        int i = ind[j];
        sum += W[i];
        int i2 = I[i];
        max_second = max(max_second, P[i2]-Z[i2]);
        while(sz(S) > max(0, need - 2*j - 2)){
            rm();
        }
        if(sz(S) + 2*j + 2 >= need){
            ans = min(ans, sum);
            if(sz(S) + 2*j + 2 > need || min_rm > 0)ans = min(ans, sum + min_rm - max_second);
        }

    }

    cout << ans << "\n";

    return 0;
}

