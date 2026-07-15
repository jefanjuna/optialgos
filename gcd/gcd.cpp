// Finds the greatest common divisor (highest common factor) between two numbers
#include <iostream>
#include <numeric>
using namespace std;
int main () {
	int a, b; cin >> a >> b;
	cout << gcd(a, b);
	return 0;
}
