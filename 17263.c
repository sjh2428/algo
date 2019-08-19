#include <stdio.h>

int main() {
	int input, N, MAX = 0;
	scanf(" %d", &N);
	for (int i = 0; i < N; i++) {
		scanf(" %d", &input);
		if (MAX < input) {
			MAX = input;
		}
	}
	printf("%d", MAX);
	return 0;
}