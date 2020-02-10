//https://www.acmicpc.net/problem/10991
#include <stdio.h>
int main() {
	int i, j, k, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (j = 0; j < n - i; j++)
			printf(" ");
		for (k = 0; k < i * 2 - 1; k++) {
			if (k % 2)
				printf(" ");
			else
				printf("*");
		}
		printf("\n");
	}
	return 0;
}