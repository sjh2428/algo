#include <stdio.h>

int main() {
    int i, t, sum = 0;
    char s;
    scanf("%d", &t);
    for(i = 1; i <= t; i++) {
        scanf(" %c", &s);
        sum += (int)(s - '0');
    }
    printf("%d\n", sum);
    return 0;
}