//https://www.acmicpc.net/problem/2522
#include <stdio.h>
int main() {
	int i, j, k, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (j = 0; j < n - i; j++)
			printf(" ");
		for (k = 0; k < i; k++)
			printf("*");
		printf("\n");
	}
	for (i = 1; i < n; i++) {
		for (j = 0; j < i; j++)
			printf(" ");
		for (k = 0; k < n - i; k++)
			printf("*");
		printf("\n");
	}
	return 0;
}