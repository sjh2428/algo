//https://www.acmicpc.net/problem/2579
#include <iostream>

using namespace std;

int main() {
	int d[301], a[301], n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> a[i];
	d[1] = a[1];
	d[2] = a[1] + a[2] > a[2] ? a[1] + a[2] : a[2];
	d[3] = a[1] + a[3] > a[2] + a[3] ? a[1] + a[3] : a[2] + a[3];
	for (int i = 3; i <= n; i++) {
		d[i] = d[i - 2] + a[i];
		if (d[i] < d[i - 3] + a[i] + a[i-1])
			d[i] = d[i - 3] + a[i] + a[i-1];
	}
	cout << d[n] << endl;

	return 0;
}