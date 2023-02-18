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


int main() {
    int n;
    cin >> n;
    set<string> proven;
    rep(c1,0,n){
        string s;
        cin >> s;
        while(s != "->"){
            if(proven.find(s) == proven.end()){
                cout << c1+1 << "\n";
                return 0;
            }
            cin >> s;
        }
        cin >> s;
        proven.insert(s);
    }
    cout << "correct\n";
    return 0;
}

