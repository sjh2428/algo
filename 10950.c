#include <stdio.h>

int main() {
    int i, n;
    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        int m, k;
        scanf("%d %d", &m, &k);
        printf("%d\n", m + k);
    }
    return 0;
}