#include <stdio.h>

int main() {
    int t, i;
    scanf("%d", &t);
    for(i = 0; i < t; i++) {
        int n, m;
        char c;
        scanf("%d%c%d", &n, &c, &m);
        printf("%d\n", n + m);
    }
    return 0;
}