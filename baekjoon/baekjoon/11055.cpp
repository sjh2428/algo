//https://www.acmicpc.net/problem/11055
#include <iostream>

using namespace std;

int main() {
	int i, j, n, A[1001], d[1001], ans;
	cin >> n;
	for (i = 0; i < n; i++)
		cin >> A[i];
	for (i = 0; i < n; i++) {
		d[i] = A[i];
		for (j = 0; j < i; j++) {
			if (A[j] < A[i] && d[i] < d[j] + A[i]) {
				d[i] = d[j] + A[i];
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