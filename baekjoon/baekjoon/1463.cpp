//https://www.acmicpc.net/problem/1463
#include <iostream>

using namespace std;

int d[1000000];

int go1(int n) {
	if (n == 1) return 0;
	if (d[n] > 0) return d[n];
	d[n] = go1(n - 1) + 1;
	if (n % 2 == 0) {
		int temp = d[n / 2] + 1;
		if (d[n] > temp)	d[n] = temp;
	}
	if (n % 3 == 0) {
		int temp = d[n / 3] + 1;
		if (d[n] > temp)	d[n] = temp;
	}
	return d[n];
}

int main() {
	int n;
	cin >> n;
	cout << go1(n) << endl;

	return 0;
}