#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	long long x = 0;
	long long y = 1;
	const int mod = 998244353;
	cout << x << "\n";
	while (n--) {
		cout << y << "\n";
		x = (x + y) % mod;
		swap(x, y);
	}
	return 0;
}
