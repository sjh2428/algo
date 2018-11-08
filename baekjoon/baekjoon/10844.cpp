//https://www.acmicpc.net/problem/10844
#include <iostream>

using namespace std;

int main() {
	long long answer = 0, n, d[101][10];
	cin >> n;
	d[1][0] = 0;
	for (int i = 1; i < 10; i++)
		d[1][i] = 1;
	
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			d[i][j] = 0;
			if (j >= 1)		d[i][j] += d[i - 1][j - 1];
			if (j <= 8)		d[i][j] += d[i - 1][j + 1];
			d[i][j] %= 1000000000;
		}
	}
	for (int i = 0; i < 10; i++)
		answer += d[n][i];
	answer %= 1000000000;
	cout << answer << endl;

	return 0;
}