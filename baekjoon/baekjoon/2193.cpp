//https://www.acmicpc.net/problem/2193
#include <iostream>

using namespace std;

int main() {
	int n;
	unsigned long long int d[91];
	cin >> n;
	d[0] = 0;
	d[1] = 1;
	for (int i = 2; i <= n; i++) 
		d[i] = d[i - 1] + d[i - 2];
	cout << d[n] << endl;

	return 0;
}