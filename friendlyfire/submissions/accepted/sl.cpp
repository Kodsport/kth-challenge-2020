#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int Time;
struct Ship {
	int x1, x2;
};
struct Area {
	mutable int x1, x2, t;
	int startt, old1, old2, index;
	void update(int to) const {
		x1 -= to - t;
		x2 += to - t;
		t = to;
	}
	void update() const {
		if (t != Time) update(Time);
	}
};

bool operator<(const Area& a, const Area& b) {
	a.update();
	b.update();
	return pii(a.x1, a.x2) < pii(b.x1, b.x2);
}

int main() {
	cin.sync_with_stdio(false);
	cin.exceptions(cin.failbit);
	int N, M;
	cin >> N >> M;
	vector<vector<Ship>> ships(N);
	rep(i,0,M) {
		int x1, x2, t;
		cin >> x1 >> x2 >> t;
		x2++;
		ships[t].push_back({x1, x2});
	}
	multiset<Area> active;
	vector<Area> allAreas;
	auto alloc = [&](int x1, int x2, int old1, int old2) -> Area {
		assert(x1 < x2); // no empty areas
		int ind = sz(allAreas);
		Area ret{x1, x2, Time, Time, old1, old2, ind};
		allAreas.push_back(ret);
		return ret;
	};
	Area initialArea = alloc(0, 1, -1, -1);
	active.insert(initialArea);

	const int inf = 1'000'000'000;
	for (int t = 1; t < N; t++) {
		Time = t;
		auto glue = [&](multiset<Area>::iterator& it) -> bool {
			it->update();
			auto next = it;
			++next;
			if (next == active.end()) return false;
			next->update();
			if (it->x2 < next->x1) return false;
			Area na = alloc(it->x1, next->x2, it->index, next->index);
			active.erase(it);
			it = active.insert(na);
			active.erase(next);
			return true;
		};
		for (Ship sh : ships[t]) {
			assert(sh.x1 < sh.x2);
			auto it = active.lower_bound({sh.x1, -inf, t});
			while (it != active.end() && glue(it)) {}
			rep(_,0,2) while (it != active.begin()) {
				--it;
				if (!glue(it)) break;
			}

			it = active.lower_bound({sh.x1, -inf, t});
			while (it != active.end()) {
				// check for overlap on right
				it->update();
				Area old = *it;
				if (old.x1 >= sh.x2) break;
				if (old.x2 <= sh.x2) {
					// remove interval completely, keep on going
					it = active.erase(it);
				}
				else {
					// keep interval partially
					while (glue(it)) {}
					old = *it;
					it = active.erase(it);
					it = active.insert(it, alloc(sh.x2, old.x2, old.index, -1));
					break;
				}
			}
			auto it2 = active.lower_bound({sh.x1, -inf, t});
			assert(it == it2);
			if (it != active.begin()) {
				// check for overlap on left, or across whole interval
				--it;
				it->update();
				Area old = *it;
				assert(old < (Area{sh.x1, -inf, t}));
				assert(old.x1 < sh.x1);
				if (old.x2 > sh.x1) {
					it = active.erase(it);
					active.insert(it, alloc(old.x1, sh.x1, old.index, -1));
					if (old.x2 > sh.x2) {
						active.insert(it, alloc(sh.x2, old.x2, old.index, -1));
					}
				}
			}
		}
	}

	if (active.empty()) {
		cout << "impossible" << endl;
	} else {
		Time = N;
		Area cur = *active.begin();
		cur.update();
		int x = cur.x1;
		int y = N;
		string out;
		while (y != 0) {
			cur.update(y);
			assert(y >= cur.startt);
			assert(cur.x1 <= x && x < cur.x2);
			while (y != cur.startt) {
				assert(cur.x1 <= x && x < cur.x2);
				cur.x1++;
				cur.x2--;
				char ch;
				if (x < cur.x1) ch = '-', x++;
				else if (x >= cur.x2) ch = '+', x--;
				else ch = '0';
				out += ch;
				y--;
			}
			if (y == 0) break;
			assert(cur.old1 != -1);
			Area next = allAreas[cur.old1];
			next.update(y);
			if (!(next.x1 <= x && x < next.x2)) {
				assert(cur.old2 != -1);
				next = allAreas[cur.old2];
				next.update(y);
				assert(next.x1 <= x && x < next.x2);
			}
			cur = next;
		}
		assert(x == 0);
		reverse(all(out));
		cout << out << endl;
	}
	exit(0);
}
