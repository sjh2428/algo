//https://www.acmicpc.net/problem/11052
#include <stdio.h>

int d[1001], p[1001];

int main() {
	int i, j, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
		scanf(" %d", &p[i]);
	
	for (i = 1; i <= n; i++)
		for (j = 1; j <= i; j++)
			if (d[i] < d[i - j] + p[j])
				d[i] = d[i - j] + p[j];

	printf("%d\n", d[n]);

	return 0;
}