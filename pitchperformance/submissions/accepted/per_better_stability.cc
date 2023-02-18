#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Real;

// integrate ax^2+bx+c from x0 to x1
Real integrate(Real x0, Real x1, Real a, Real b, Real c) {
    Real dx = x1-x0;
    return dx*(a*(x0*x0 + dx*x0 + dx*dx/3.0) + b*(x0 + dx/2.0) + c);
}

// integrate |ax^2+bx+c| from x0 to x1
Real integrate_abs(Real x0, Real x1, Real a, Real b, Real c) {
    vector<Real> X(1, x0);
    if (a && b*b > 4*a*c) {
        Real mid = -b/(2.0*a), offs = sqrtl(b*b - 4*a*c)/(2.0*fabsl(a));
        if (mid-offs > x0 && mid-offs < x1) X.push_back(mid-offs);
        if (mid+offs > x0 && mid+offs < x1) X.push_back(mid+offs);
    } else if (!a && b) {
        Real x = -1.0*c/b;
        if (x > x0 && x < x1) X.push_back(x);
    }
    X.push_back(x1);
    Real ans = 0;
    for (int i = 1; i < X.size(); ++i)
        ans += fabsl(integrate(X[i-1], X[i], a, b, c));
    return ans;
}

int main(void) {
    vector<pair<ll, int>> E;
    int n;
    cin >> n;
    vector<ll> xf(n+1), yf(n+1);
    for (int i = 1; i <= n; ++i) {
        cin >> xf[i] >> yf[i];
        E.push_back(make_pair(xf[i], 0));
    }

    int m;
    cin >> m;
    vector<ll> xg(m+1), ag(m+1), bg(m+1), cg(m+1);
    for (int i = 1; i <= m; ++i) {
        cin >> xg[i] >> ag[i] >> bg[i] >> cg[i];
        E.push_back(make_pair(xg[i], 1));
    }

    sort(E.begin(), E.end());
    int i = 1, j = 1;
    ll x0 = 0;
    Real ans = 0;
    for (auto &e: E) {
        ll x1 = e.first;
        ans += integrate_abs(x0, x1, ag[j], bg[j], cg[j]-yf[i]);
        if (e.second) ++j;
        else ++i;
        x0 = x1;
    }

    cout << setprecision(15) << ans << endl;
}
