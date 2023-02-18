#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

double eval2(double fx, double tx, double a, double b, double c) {
    double T = a * pow(tx, 3) / 3 +
        b * pow(tx, 2) / 2 +
        c * tx;
    double F = a * pow(fx, 3) / 3 +
        b * pow(fx, 2) / 2 +
        c * fx;
    return fabs(T - F);
}

double eval(int fx, int tx, int y, int a, int b, int c) {
    c -= y;

    double disc = double(b) * b - 4.0 * a * c;
    vector<double> intervals;
    intervals.push_back(fx);
    if (disc >= 0) {
        double x0 = (-b - sqrt(disc)) / 2 / a;
        double x1 = (-b + sqrt(disc)) / 2 / a;
        if (fx <= x0 && x0 <= tx) intervals.push_back(x0);
        if (fx <= x1 && x1 <= tx) intervals.push_back(x1);
    }
    intervals.push_back(tx);
    sort(all(intervals));
    double res = 0;
    for (int i = 0; i < sz(intervals) - 1; i++) {
        res += eval2(intervals[i], intervals[i + 1], a, b, c);
    }
    return res;
}

int main() {
	cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);

    vector<pair<int, bool>> BG;

    int N;
    cin >> N;
    vi X(N), Y(N);
    rep(i,0,N) {
        cin >> X[i] >> Y[i];
        BG.emplace_back(X[i], true);
    }

    int M;
    cin >> M;
    vi XP(M), A(M), B(M), C(M);
    rep(i,0,M) {
        cin >> XP[i] >> A[i] >> B[i] >> C[i];
        BG.emplace_back(XP[i], false);
    }

    sort(all(BG));

    int n = 0;
    int m = 0;
    int tx = 0;
    double res = 0;
    for (int i = 0; i < sz(BG) - 1; i++) {
        int nx = BG[i].first;

        res += eval(tx, nx, Y[n], A[m], B[m], C[m]);

        if (BG[i].second) n++;
        else m++;
        tx = nx;
    }
    cout << fixed << setprecision(10) << res << endl;
}
