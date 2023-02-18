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

int n,m;

vector<double> A,B,C,Y,X1,X2;
double eps = 0.0000000001;

double F(double a, double b, double c, double x){
    return a*x*x*x/3.0 + b*x*x/2.0 + c*x;
}

double integrate(double y, double a, double b, double c, double x1, double x2){
    double i1 = x1;
    double i2 = x1;
    if(abs(a) < eps){
        if(abs(b) > eps){
            i1 = (y-c)/b;
        }
    }
    else{
        double p = b/a;
        double q = (c-y)/a;
        double D = (p*p)/4.0 - q;
        if(abs(D) < eps){
            i1 = -p/2.0;
        }
        else{
            if(D > 0){
                i1 = sqrt(D) - p/2.0;
                i2 = -sqrt(D) - p/2.0;
            }
        }
    }
    i1 = max(i1, x1);
    i2 = max(i2, x1);
    i1 = min(i1, x2);
    i2 = min(i2, x2);
    if(i1 > i2)swap(i1,i2);
    double res = 0.0;
    res += abs(F(a,b,c-y,i1) - F(a,b,c-y,x1));
    res += abs(F(a,b,c-y,i2) - F(a,b,c-y,i1));
    res += abs(F(a,b,c-y,x2) - F(a,b,c-y,i2));
    return res;
}

int main() {
    cin >> n;
    rep(c1,0,n){
        int x,y;
        cin >> x >> y;
        X1.push_back(x);
        Y.push_back(y);
    }
    cin >> m;
    rep(c1,0,m){
        int x,a,b,c;
        cin >> x >> a >> b >> c;
        X2.push_back(x);
        A.push_back(a);
        B.push_back(b);
        C.push_back(c);
    }

    int l = 0;
    int r = 0;
    double prev = 0.0;

    double ans = 0.0;
    double a = A[0];
    double b = B[0];
    double c = C[0];
    double y = Y[0];
    while(l < sz(X1) && r < sz(X2)){
        if(X1[l] < X2[r]){
            double x = X1[l];
            ans += integrate(y,a,b,c,prev,x);
            l++;
            if(l < n)y = Y[l];
            prev = x;
        }
        else{
            double x = X2[r];
            ans += integrate(y,a,b,c,prev,x);
            r++;
            if(r < m){
                a = A[r];
                b = B[r];
                c = C[r];
            }
            prev = x;
        }
    }
    cout << setprecision(18) << ans << "\n";

    return 0;
}
