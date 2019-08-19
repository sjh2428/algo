//https://www.acmicpc.net/problem/11722
#include <iostream>

using namespace std;

int main() {
	int i, j, n, A[1001], d[1001], ans;
	cin >> n;
	for (i = n - 1; i >= 0; i--)
		cin >> A[i];
	for (i = 0; i < n; i++) {
		d[i] = 1;
		for (j = 0; j < i; j++) {
			if (A[j] < A[i] && d[i] < d[j] + 1) {
				d[i] = d[j] + 1;
			}
		}
	}
	ans = d[0];
	for (i = 1; i < n; i++)
		if (ans < d[i])
			ans = d[i];
	cout << ans << endl;

	return 0;
}