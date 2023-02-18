#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// integrate ax^2+bx+c from x0 to x1
double integrate(double x0, double x1, double a, double b, double c) {
    return a*(x1*x1*x1-x0*x0*x0)/3.0 + b*(x1*x1-x0*x0)/2.0 + c*(x1-x0);
}

// integrate |ax^2+bx+c| from x0 to x1
double integrate_abs(ll x0, ll x1, double a, double b, double c) {
    vector<double> X(1, x0);
    if (a && b*b > 4*a*c) {
        double mid = -b/(2.0*a), offs = sqrt(b*b - 4*a*c)/(2.0*fabs(a));
        if (mid-offs > x0 && mid-offs < x1) X.push_back(mid-offs);
        if (mid+offs > x0 && mid+offs < x1) X.push_back(mid+offs);
    } else if (!a && b) {
        double x = -1.0*c/b;
        if (x > x0 && x < x1) X.push_back(x);
    }
    X.push_back(x1);
    double ans = 0;
    for (int i = 1; i < X.size(); ++i)
        ans += fabs(integrate(X[i-1], X[i], a, b, c));
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
    double ans = 0;
    for (auto &e: E) {
        ll x1 = e.first;
        ans += integrate_abs(x0, x1, ag[j], bg[j], cg[j]-yf[i]);
        if (e.second) ++j;
        else ++i;
        x0 = x1;
    }

    printf("%.15lf\n", ans);
}
