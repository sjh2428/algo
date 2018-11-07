//https://www.acmicpc.net/problem/2444
#include <stdio.h>
int main() {
	int i, j, k, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (k = 0; k < n - i; k++)
			printf(" ");
		for (j = 0; j < (i * 2) - 1; j++)
			printf("*");
		printf("\n");
	}
	for (i = 1; i < n; i++) {
		for (k = 0; k < i; k++)
			printf(" ");
		for (j = 0; j < ((n - 1) * 2) - (2 * i - 1); j++)
			printf("*");
		printf("\n");
	}
	return 0;
}