#include <bits/stdc++.h>
using namespace std;
const char *sym = "-0+";

struct boat {
    int x1, x2, y, idx;

    int midx2() const { return x1 + x2; }
    int lasty() const { return max(0, y - (x2 - x1)/2); }
    
    bool operator<(const boat &b) const {
        if (midx2() != b.midx2()) return midx2() < b.midx2();
        if (y != b.y) return y < b.y;
        return x1 < b.x1;
    }

    bool touches(const boat &b) const {
        return x2 >= b.x1 + (b.y - y) - 1 && x1 <= b.x2 - (b.y - y) + 1;
    }

    bool contains(int px, int py) const {
        return x1 + (y-py) <= px && px <= x2 - (y-py);
    }
};
    
int main(void) {
    int n, m;
    scanf("%d%d", &n, &m);
    vector<boat> B(m);
    vector<int> tops[n+1];
    set<int> bots[n+1];
    for (int i = 0; i < m; ++i) {
        B[i].idx = i;
        scanf("%d%d%d", &B[i].x1, &B[i].x2, &B[i].y);
        tops[B[i].y].push_back(i);
    }
    
    set<boat> cur;
    auto cut = [&](int i, int y) {
        bots[B[i].lasty()].erase(i);
        if (y <= B[i].y) bots[y].insert(i);
    };
    auto covered = [&](int x, int y) {
        auto it = cur.upper_bound({x,x,y});
        return (it != cur.end() && it->contains(x, y) ||
                it != cur.begin() && (--it)->contains(x, y));
    };
    for (int y = n; y > 0; --y) {
        for (int i: tops[y]) {
            auto it = cur.upper_bound({B[i].x1, B[i].x1, B[i].y});
            if (it != cur.begin() && !B[i].touches(*--it)) ++it;
            while (it != cur.end() && B[i].touches(*it)) {
                B[i].x2 = max(B[i].x2, it->x2 - (it->y - y));
                B[i].x1 = min(B[i].x1, it->x1 + (it->y - y));
                cut(it->idx, y+1);
                cur.erase(it++);
            }
            cur.insert(B[i]);
            bots[B[i].lasty()].insert(i);
        }
        for (int i: bots[y]) cur.erase(B[i]);
    }

    if (covered(0, 0)) {
        printf("impossible\n");
        return 0;
    }

    string sol;
    int x = 0;
    for (int y = 1; y <= n; ++y) {
        for (int i: bots[y]) cur.insert(B[i]);
        for (int nx = x-1; nx <= x+1; ++nx)
            if (!covered(nx, y)) {
                sol += sym[nx-x+1];
                x = nx;
                break;
            }
        for (int i: tops[y]) cur.erase(B[i]);
    }
    printf("%s\n", sol.c_str());
    
}
