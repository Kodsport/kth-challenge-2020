// NB! this does not solve the lexicographically smallest variant,
// just finds one optimal solution
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
    vector<int> seq, taken(n+1, false);
    // Take components with trees by going greedily from each leaf and
    // take successors while still available.
    for (int i = 1; i <= n; ++i)
        if (back[i].empty())
            for (int j = i; !taken[j]; taken[j] = true, j = forw[j])
                seq.push_back(j);
    // Only thing remaining are cycles. Start anywhere and take the
    // entire cycle in order.
    for (int i = 1; i <= n; ++i)
        for (int j = i; !taken[j]; taken[j] = true, j = forw[j])
            seq.push_back(j);
    vector<int> sol(n+1);
    for (int i = 0; i < n; ++i)
        sol[seq[i]] = seq[(i+1)%n];
    
    for (int i = 1; i <= n; ++i)
        printf("%d%c", sol[i], i==n ? '\n' : ' ');
}
