#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
	cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);

    string s;
    cin >> s;
    rep(i,0,sz(s)/3) {
        vector<char> c;
        rep(j,0,3) c.push_back(s[sz(s) / 3 * j + i]);
        sort(all(c));
        cout << c[1];
    }
    cout << endl;
}
