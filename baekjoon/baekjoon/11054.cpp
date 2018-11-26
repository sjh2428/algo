//https://www.acmicpc.net/problem/11054
#include <iostream>

using namespace std;

int main() {
	int i, j, N, A[1001], d1[1001], d2[1001], max = 0;
	cin >> N;
	for (i = 1; i <= N; i++)
		cin >> A[i];
	for (i = 1; i <= N; i++) {
		d1[i] = 1;
		for(j = 1; j <= i; j++)
			if (A[j] < A[i] && d1[i] < d1[j] + 1)
				d1[i]++;
	}
		
	for (i = N; i >= 1; i--) {
		d2[i] = 1;
		for(j = N; j >= i; j--)
			if (A[j] < A[i] && d2[i] < d2[j] + 1)
				d2[i]++;
	}
	
	for (i = 1; i <= N; i++)
		if (max < (d1[i] + d2[i] - 1))
			max = d1[i] + d2[i] - 1;
	
	cout << max << endl;
	
	return 0;
}