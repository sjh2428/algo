//https://www.acmicpc.net/problem/11057
#include <iostream>

using namespace std;

int main() {
	int d[1001][10], answer = 0;
	int n;
	cin >> n;
	for (int i = 0; i < 10; i++)
		d[1][i] = 1;
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			d[i][j] = 0;
			for (int k = 0; k <= j; k++)
				d[i][j] += d[i - 1][k];
			d[i][j] %= 10007;
		}
	}
	for (int i = 0; i < 10; i++)
		answer += d[n][i];
	answer %= 10007;
	cout << answer << endl;
	return 0;
}