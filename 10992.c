////https://www.acmicpc.net/problem/10992
#include <stdio.h>
int main() {
	int i, j, k, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		if (i == 1) {
			for (j = 0; j < n - i; j++)
				printf(" ");
			printf("*");
		}
		else if (1 < i && i < n) {
			for (j = 0; j < n - i; j++)
				printf(" ");
			printf("*");
			for (j = 0; j < i * 2 - 3; j++)
				printf(" ");
			printf("*");
		}
		else if (i == n)
			for (k = 0; k < n * 2 - 1; k++)
				printf("*");
		printf("\n");
	}
	return 0;
}