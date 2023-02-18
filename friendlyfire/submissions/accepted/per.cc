#include <bits/stdc++.h>
using namespace std;
const char *sym = "-0+";

struct boat {
    int idx, x1, x2, y;

    int midx2() const { return x1 + x2; }
    int lasty() const { return max(0, y - (x2 - x1)/2); }
    
    bool operator<(const boat &b) const {
        if (midx2() != b.midx2()) return midx2() < b.midx2();
        if (y != b.y) return y < b.y;
        return x1 < b.x1;
    }

    bool touches(const boat &b) const {
        if (y > b.y) return b.touches(*this);
        return x2 >= b.x1 + (b.y - y) - 1 && x1 <= b.x2 - (b.y - y) + 1;
    }

    bool dominates(const boat &b) const {
        return y >= b.y && x1 <= b.x1 - (y-b.y) && x2 >= b.x2 + (y-b.y);
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
    auto covered = [&](const boat &b) {
        auto it = cur.upper_bound(b);
        if (it != cur.end() && it->dominates(b)) return true;
        if (it != cur.begin() && (--it)->dominates(b)) return true;
        return false;
    };
    for (int y = n; y > 0; --y) {
        for (auto &i: tops[y]) {
            if (covered(B[i])) continue;
            auto it = cur.upper_bound(B[i]);
            while (it != cur.end() && B[i].touches(*it)) {
                B[i].x2 = max(B[i].x2, it->x2 - (it->y - y));
                cut(it->idx, y+1);
                cur.erase(it++);
            }
            if (it != cur.begin()) {
                --it;
                while (it != cur.end() && B[i].touches(*it)) {
                    B[i].x1 = min(B[i].x1, it->x1 + (it->y - y));
                    cut(it->idx, y+1);
                    cur.erase(it++);
                    if (it != cur.begin()) --it;
                }
            }
            cur.insert(B[i]);
            bots[B[i].lasty()].insert(i);
        }
        for (auto &i: bots[y]) cur.erase(B[i]);
    }

    boat torpedo = {0, 0, 0, 0};
    if (covered(torpedo)) {
        printf("impossible\n");
        return 0;
    }

    string sol;
    for (int y = 1; y <= n; ++y) {
        for (auto &i: bots[y]) cur.insert(B[i]);
        int x = torpedo.x1;
        for (int nx = x-1; nx <= x+1; ++nx) {
            torpedo = {0, nx, nx, y};
            if (!covered(torpedo)) {
                sol += sym[nx-x+1];
                break;
            }
        }
        assert(sol.length() == y);
        for (auto &i: tops[y]) {
            assert(!B[i].dominates(torpedo));
            cur.erase(B[i]);
        }
    }
    printf("%s\n", sol.c_str());
    
}
