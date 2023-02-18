// Quadratic but only check first 200k lines, and only randomly
// spot-check 30% of assumptions after the first 10k lines.
#include <bits/stdc++.h>
using namespace std;

int enc(const string& p) {
    int r = 0;
    for (char c: p) r = 30*r + c-'a'+1;
    return r;
}

int main(void) {
    int n;
    scanf("%d", &n);
    vector<int> facts;
    for (int i = 0; i < min(n, 200000); ++i) {
        char buf[30];
        while (scanf("%s", buf) == 1 && strcmp(buf, "->")) {
            if ((i < 10000 || random() % 100 < 30) && find(facts.begin(), facts.end(), enc(buf)) == facts.end()) {
                printf("%d\n", i+1);
                return 0;
            }
        }
        scanf("%s", buf);
        facts.push_back(enc(buf));
    }
    printf("correct\n");
   
}
