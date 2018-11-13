//https://www.acmicpc.net/problem/1699
#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int d[100001] = {0, };
	for (int i = 0; i <= n; i++) {
		d[i] = i;
		for (int j = 1; j*j <= i; j++)
			if (d[i] > d[i - (j*j)] + 1)
				d[i] = d[i - (j*j)] + 1;
	}
	cout << d[n] << endl;

	return 0;
}