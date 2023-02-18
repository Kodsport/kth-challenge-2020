#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

ll naive(int days) {
	if (days < 4) return 0;
	return 3LL << ((days - 4) / 3 * 2);
}

ll solve(int remdays, ll curbling, ll curnormal, ll curexotic, array<ll, 3> numNormal, array<ll, 3> numExotic);

map<tuple<int, ll, array<ll, 3>, array<ll, 3>>, ll> mem;
ll solve5(int remdays, ll curbling, array<ll, 3> numNormal, array<ll, 3> numExotic) {
	auto key = make_tuple(remdays, curbling, numNormal, numExotic);
	ll& out = mem[key];
	if (out) return out - 1;
	ll ret = solve(remdays, curbling, 0, 0, numNormal, numExotic);
	out = ret + 1;
	return ret;
}

ll solve4(int remdays, ll curbling, array<ll, 3> numNormal, array<ll, 3> numExotic) {
	if (remdays == 1) return curbling;
	ll gain = naive(remdays);
	ll add = 0;
	if (numExotic[0] > 1) {
		add += gain * (numExotic[0] - 1) * 500;
		numExotic[0] = 1;
	}
	if (numNormal[0] > 4) {
		add += gain * (numNormal[0] - 4) * 100;
		numNormal[0] = 4;
	}
	if (curbling > remdays * 400) {
		ll diff = curbling - remdays * 400;
		add += diff;
		curbling -= diff;
	}
	rotate(numNormal.begin(), numNormal.begin() + 1, numNormal.end());
	rotate(numExotic.begin(), numExotic.begin() + 1, numExotic.end());
	return solve5(remdays - 1, curbling, numNormal, numExotic) + add;
}

ll solve3(int remdays, ll curbling, array<ll, 3> numNormal, array<ll, 3> numExotic) {
	ll r = solve4(remdays, curbling, numNormal, numExotic);
	if (curbling >= 400) {
		r = max(r, solve4(remdays, curbling + 100, numNormal, numExotic));
		numExotic[0]++;
		r = max(r, solve4(remdays, curbling - 400, numNormal, numExotic));
	}
	return r;
}

ll solve2(int remdays, ll curbling, ll curnormal, ll curexotic, array<ll, 3> numNormal, array<ll, 3> numExotic) {
	if (remdays <= 3) {
		// in the end-phase it's not worth planting anything
		return solve3(remdays, curbling + 100 * curnormal + 500 * curexotic, numNormal, numExotic);
	}

	ll res = 0;
	rep(sellnormal,0,12+1) rep(sellexotic,0,3+1) {
		if (sellnormal > curnormal || sellexotic > curexotic) continue;
		// everything that's not sold for bling we should just re-plant
		array<ll, 3> numNormal2 = numNormal;
		array<ll, 3> numExotic2 = numExotic;
		numNormal2[0] += curnormal - sellnormal;
		numExotic2[0] += curexotic - sellexotic;
		ll r = solve3(remdays, curbling + 100 * sellnormal + 500 * sellexotic, numNormal2, numExotic2);
		res = max(res, r);
	}
	return res;
}

ll solve(int remdays, ll curbling, ll curnormal, ll curexotic, array<ll, 3> numNormal, array<ll, 3> numExotic) {
	return solve2(remdays, curbling, curnormal + 3 * numNormal[0], curexotic + 3 * numExotic[0], numNormal, numExotic);
}

int main() {
	cin.sync_with_stdio(false);
	cin.exceptions(cin.failbit);
	int remdays;
	ll curbling, curnormal;
	cin >> remdays >> curbling >> curnormal;
	array<ll, 3> numNormal;
	rep(i,0,3) cin >> numNormal[i];
	cout << solve(remdays, curbling, curnormal, 0, numNormal, {0, 0, 0}) << endl;
	exit(0);
}
