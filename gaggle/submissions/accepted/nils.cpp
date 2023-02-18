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

int n;
vi A, start, stop;
set<int> S;

int main() {
    cin >> n;
    rep(c1,0,n){
        int a;
        cin >> a;
        a--;
        A.push_back(a);
        start.push_back(c1);
        stop.push_back(c1);
        S.insert(c1);
    }
    rep(c1,0,n-1){
        int ans = -1;
        if(start[A[c1]] == A[c1] && stop[A[c1]] != c1){
            ans = A[c1];
            S.erase(ans);
        }
        else{
            ans = *S.begin();
            S.erase(ans);
            if(stop[ans] == c1){
                int ans2 = *S.begin();
                S.erase(ans2);
                S.insert(ans);
                ans = ans2;
            }
        }
        cout << ans+1 << " ";
        start[stop[ans]] = start[c1];
        stop[start[c1]] = stop[ans];
        start[ans] = start[c1];
    }
    cout << *S.begin()+1 << "\n";
    return 0;
}
