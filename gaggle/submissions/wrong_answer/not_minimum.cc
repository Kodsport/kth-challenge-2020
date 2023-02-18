#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    scanf("%d", &n);
    vector<int> forw(n+1);
    vector<vector<int>> back(n+1);
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &forw[i]);
        back[forw[i]].push_back(i);
    }
    vector<int> orig_forw = forw;
    
    for (int i = 1; i <= n; ++i)
        sort(back[i].begin(), back[i].end());
    
    vector<int> in_cycle(n+1, false);
    vector<int> marked(n+1, false);
    for (int i = 1; i <= n; ++i)
        if (!marked[i]) {
            int j = i;
            while (!marked[j]) {
                marked[j] = i;
                j = forw[j];
            }
            if (marked[j] == i)
                while (!in_cycle[j]) {
                    in_cycle[j] = true;
                    j = forw[j];
                }
        }

    fill(marked.begin(), marked.end(), 0);
    for (int i = 1; i <= n; ++i)
        if (in_cycle[i] && !marked[i]) {
            bool has_exit = false;
            int min_i = n+1, min_branching_i = n+1;
            int j = i;
            while (!marked[j]) {
                marked[j] = true;
                has_exit |= !in_cycle[back[j][0]];
                min_i = min(min_i, j);
                if (back[j].size() > 1)
                    min_branching_i = min(min_branching_i, j);
                j = forw[j];
            }
            if (!has_exit) {
                //if (min_branching_i < n+1)
                //    min_i = min_branching_i;
                forw[back[min_i].front()] = -1;
                back[min_i].erase(back[min_i].begin());
            }
        }

    for (int i = 1; i <= n; ++i) {
        while (back[i].size() > 1) {
            forw[back[i].back()] = -1;
            back[i].pop_back();
        }
    }

    vector<int> avail_dsts, avail_srcs, other_end(n+1, -1);
    for (int i = 1; i <= n; ++i) {
        if (back[i].empty()) {
            int j = i;
            while (forw[j] != -1) j = forw[j];
            other_end[i] = j;
            other_end[j] = i;
            avail_dsts.push_back(j);
            avail_srcs.push_back(i);
        }
    }

    sort(avail_dsts.begin(), avail_dsts.end());
    sort(avail_srcs.begin(), avail_srcs.end(), greater<int>());

    for (auto &dst: avail_dsts) {
        auto src = avail_srcs.end() - 1;
        if (src != avail_srcs.begin() && other_end[*src] == dst) --src;
        int dst_end = other_end[dst], src_end = other_end[*src];
        other_end[dst_end] = src_end;
        other_end[src_end] = dst_end;
        forw[dst] = *src;
        avail_srcs.erase(src);
    }

    for (int i = 1; i <= n; ++i)
        printf("%d%c", forw[i], i==n ? '\n' : ' ');
}
