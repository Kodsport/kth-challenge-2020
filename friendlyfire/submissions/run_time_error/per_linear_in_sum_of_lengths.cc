#include <bits/stdc++.h>
using namespace std;
const char *sym = "-0+";
typedef pair<int, int> pii;

int main(void) {
    int n, m;
    scanf("%d%d", &n, &m);
    vector<pii> ivals[n+1];
    for (int i = 0; i < m; ++i) {
        int x1, x2, y;
        scanf("%d%d%d", &x1, &x2, &y);
        ivals[y].push_back(pii(x1, x2));
    }
    for (int y = n; y > 0; --y) {
        auto &Is = ivals[y];
        int at = 0;
        sort(Is.begin(), Is.end());
        for (int i = 0; i < Is.size(); ++i)
            if (Is[i].first <= Is[at].second+1)
                Is[at].second = max(Is[at].second, Is[i].second);
            else
                Is[++at] = Is[i];
        Is.resize(at+1);
        for (auto &I: Is)
            if (I.first+1 <= I.second-1)
                ivals[y-1].push_back(pii(I.first+1, I.second-1));
    }

    auto covered = [](const vector<pii> &Is, int x) -> bool {
        auto it = upper_bound(Is.begin(), Is.end(), pii(x, 1<<30));
        return it != Is.begin() && ((--it)->second >= x);
    };

    if (covered(ivals[0], 0)) {
        printf("impossible\n");
        return 0;
    }

    int x = 0;
    string sol;
    for (int y = 1; y <= n; ++y) {
        for (int nx = x-1; nx <= x+1; ++nx) {
            if (!covered(ivals[y], nx)) {
                sol += sym[nx-x+1];
                x = nx;
                break;
            }
        }
    }
    printf("%s\n", sol.c_str());
    
}
