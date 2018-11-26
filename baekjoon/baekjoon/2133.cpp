//https://www.acmicpc.net/problem/2133
#include <iostream>

using namespace std;

int main() {
	int i, j, n, d[31];
	cin >> n;
	d[0] = 1;
	d[1] = 0;
	for (i = 2; i <= n; i++) {
		if (i % 2 == 0) {
			d[i] = 3 * d[i - 2];
			for (j = 4; j <= i; j += 2) {
				d[i] += 2 * d[i - j];
			}
		}
		else
			d[i] = 0;
	}
	cout << d[n] << endl;
	return 0;
}