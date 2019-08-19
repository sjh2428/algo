//https://www.acmicpc.net/problem/2446
#include <stdio.h>
int main() {
	int i, j, k, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (j = 0; j < i - 1; j++)
			printf(" ");
		for (k = 0; k < (n * 2 - 1) - ((i - 1) * 2); k++)
			printf("*");
		printf("\n");
	}
	for (i = 1; i < n; i++) {
		for (j = 0; j < n - 1 - i; j++)
			printf(" ");
		for (k = 0; k < i * 2 + 1; k++)
			printf("*");
		printf("\n");
	}
	return 0;
}