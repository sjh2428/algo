#include <stdio.h>

int main() {
    char s;
    int cnt = 0;
    while((s = getchar()) != EOF) {
        putchar(s);
        cnt++;
        if(cnt % 10 == 0)
            printf("\n");
    }
    return 0;
}