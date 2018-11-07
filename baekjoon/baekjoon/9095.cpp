#include <stdio.h>

int d[11];
int add(int n) {
	int i;
	d[0] = 1;
	d[1] = 1;
	d[2] = 2;
	for (i = 3; i <= n; i++)
		d[i] = d[i - 1] + d[i - 2] + d[i - 3];
	return d[n];
}

int main() {
	int i, T, n;
	scanf(" %d", &T);
	for (i = 0; i < T; i++) {
		scanf(" %d", &n);
		printf("%d\n", add(n));
	}

	return 0;
}