#include <stdio.h>

int main() {
	int n, cnt = 0;
	char c[51];
	scanf(" %d", &n);
	for (int i = 0; i < n; i++) {
		scanf(" %s", c);
		cnt = 0;
		for (int j = 0; c[j] != '\0'; j++) {
			if (c[j] == '(')
				cnt += 1;
			else if (c[j] == ')')
				cnt -= 1;
			if (cnt < 0)
				break;
		}
		if (cnt == 0)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}