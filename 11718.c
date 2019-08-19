#include <stdio.h>

int main() {
    char str;
    while((str = getchar()) != EOF) {
        putchar(str);
    }
    return 0;
}