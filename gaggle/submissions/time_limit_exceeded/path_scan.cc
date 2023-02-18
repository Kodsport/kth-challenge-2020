#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    scanf("%d", &n);
    vector<int> orig_forw(n+1), forw(n+1, -1);
    for (int i = 1; i <= n; ++i)
        scanf("%d", &orig_forw[i]);
    
    
    vector<int> avail, taken(n+1, 0), other_end(n+1, -1);
    for (int i = n; i >= 1; --i) {
        other_end[i] = i;
        avail.push_back(i);
    }

    auto slow_fast_forward = [&](int i) {
        while (forw[i] != -1) i = forw[i];
        return i;
    };
    
    for (int i = 1; i <= n; ++i) {
        if (!taken[orig_forw[i]] && slow_fast_forward(orig_forw[i]) != i) {
            forw[i] = orig_forw[i];
            taken[orig_forw[i]] = true;
            continue;
        }
        int x = -1;
        while (taken[avail.back()] || (i < n && slow_fast_forward(avail.back()) == i)) {
            if (!taken[avail.back()]) x = avail.back();
            avail.pop_back();
        }
        int j = avail.back();
        avail.pop_back();
        if (x != -1) avail.push_back(x);
        forw[i] = j;
        taken[j] = true;
    }

    for (int i = 1; i <= n; ++i)
        printf("%d%c", forw[i], i==n ? '\n' : ' ');
}
