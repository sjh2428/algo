#include <iostream>

using namespace std;

int main() {
	int max, n, d[100001], a[100001];
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> a[i];

	d[1] = a[1];
	max = d[1];

	for (int i = 2; i <= n; i++) {
		d[i] = a[i];
		if (d[i] < d[i - 1] + a[i])
			d[i] = d[i - 1] + a[i];
	}
	for (int i = 2; i <= n; i++)
		if (max < d[i])
			max = d[i];

	cout << max << endl;
	return 0;
}