#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    scanf("%d", &n);
    vector<int> forw(n+1);
    for (int i = 1; i <= n; ++i)
        scanf("%d", &forw[i]);
    
    vector<int> avail, taken(n+1, 0), other_end(n+1, -1);
    for (int i = n; i >= 1; --i) {
        other_end[i] = i;
        avail.push_back(i);
    }

    for (int i = 1; i <= n; ++i) {
        if (other_end[i] != forw[i])
            avail.push_back(forw[i]);
        int x = -1;
        while (taken[avail.back()] || (i < n && other_end[i] == avail.back())) {
            if (!taken[avail.back()]) x = avail.back();
            avail.pop_back();
        }
        int j = avail.back();
        avail.pop_back();
        if (x != -1) avail.push_back(x);
        int i_end = other_end[i], j_end = other_end[j];
        forw[i] = j;
        taken[j] = true;
        other_end[i_end] = j_end;
        other_end[j_end] = i_end;
    }

    for (int i = 1; i <= n; ++i)
        printf("%d%c", forw[i], i==n ? '\n' : ' ');
}
