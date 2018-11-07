//https://www.acmicpc.net/problem/2445
#include <stdio.h>
int main() {
	int i, j, k, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (j = 0; j < i; j++)
			printf("*");
		for (k = 0; k < (n - i) * 2; k++)
			printf(" ");
		for (j = 0; j < i; j++)
			printf("*");
		printf("\n");
	}
	for (i = 1; i < n; i++) {
		for (j = 0; j < n - i; j++)
			printf("*");
		for (k = 0; k < i * 2; k++)
			printf(" ");
		for (j = 0; j < n - i; j++)
			printf("*");
		printf("\n");
	}
	return 0;
}