#include <stdio.h>

int main() {
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; i++) {
        int n, m;
        scanf("%d %d", &n, &m);
        printf("Case #%d: %d + %d = %d\n", i, n, m, n + m);
    }
    return 0;
}